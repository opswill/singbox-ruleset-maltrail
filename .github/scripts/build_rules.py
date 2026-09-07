#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import ipaddress
import json
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable

IPAddress = ipaddress.IPv4Address | ipaddress.IPv6Address
IPNetwork = ipaddress.IPv4Network | ipaddress.IPv6Network


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_lines(path: Path, values: Iterable[str]) -> None:
    path.write_text("".join(f"{value}\n" for value in values), encoding="utf-8", newline="\n")


def write_json(path: Path, data: object) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def human_bytes(size: int) -> str:
    value = float(size)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if value < 1024 or unit == "GiB":
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    raise AssertionError("unreachable")


# ============================================================
# IPsum
# ============================================================


def parse_ipsum(path: Path, minimum: int) -> tuple[dict[IPAddress, int], int, int]:
    ip_counts: dict[IPAddress, int] = {}
    raw_rows = 0
    duplicate_rows = 0

    with path.open("r", encoding="utf-8", errors="strict") as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Invalid IPsum row at line {lineno}: {line!r}")

            try:
                ip = ipaddress.ip_address(parts[0])
                count = int(parts[1])
            except ValueError as exc:
                raise ValueError(f"Invalid IPsum row at line {lineno}: {line!r}: {exc}") from exc

            if count < 1:
                raise ValueError(f"Invalid occurrence count at line {lineno}: {count}")

            raw_rows += 1
            old = ip_counts.get(ip)
            if old is None:
                ip_counts[ip] = count
            elif old == count:
                duplicate_rows += 1
            else:
                raise ValueError(
                    f"Conflicting duplicate IPsum entry at line {lineno}: "
                    f"{ip} has counts {old} and {count}"
                )

    if len(ip_counts) < minimum:
        raise ValueError(
            f"IPsum sanity check failed: {len(ip_counts)} unique IPs < minimum {minimum}"
        )

    return ip_counts, raw_rows, duplicate_rows


def exact_collapse(members: set[IPAddress]) -> list[IPNetwork]:
    collapsed: list[IPNetwork] = []

    for version in (4, 6):
        networks = [
            ipaddress.ip_network(f"{ip}/{ip.max_prefixlen}")
            for ip in members
            if ip.version == version
        ]
        collapsed.extend(ipaddress.collapse_addresses(networks))

    collapsed.sort(
        key=lambda network: (
            network.version,
            int(network.network_address),
            network.prefixlen,
        )
    )

    # Safety check 1: cardinality must be identical.
    represented = sum(network.num_addresses for network in collapsed)
    if represented != len(members):
        raise ValueError(
            "CIDR cardinality check failed: "
            f"{represented} represented addresses != {len(members)} source IPs"
        )

    # Safety check 2: after the cardinality guard, expansion is bounded by
    # len(members), so an exact set comparison is safe and proves that no
    # unrelated address was introduced and no source address was lost.
    expanded: set[IPAddress] = set()
    for network in collapsed:
        expanded.update(network)
    if expanded != members:
        raise ValueError("CIDR exact-set check failed")

    return collapsed


def format_network(network: IPNetwork) -> str:
    # Plain IPs are valid in sing-box ip_cidr and are smaller than /32 or /128.
    if network.prefixlen == network.max_prefixlen:
        return str(network.network_address)
    return str(network)


# ============================================================
# Maltrail domains
# ============================================================


def parse_domains(path: Path, minimum: int) -> tuple[set[str], int, int]:
    domains: set[str] = set()
    raw_rows = 0
    duplicate_rows = 0

    with path.open("r", encoding="utf-8", errors="strict") as f:
        for lineno, raw in enumerate(f, 1):
            domain = raw.strip()
            if not domain or domain.startswith("#"):
                continue

            raw_rows += 1
            domain = domain.lower()

            if domain.startswith(".") or "*" in domain:
                raise ValueError(f"Unexpected wildcard/prefixed domain at line {lineno}: {domain!r}")
            if domain.endswith("."):
                raise ValueError(f"Unexpected trailing dot at line {lineno}: {domain!r}")
            if any(ch.isspace() for ch in domain):
                raise ValueError(f"Whitespace in domain at line {lineno}: {domain!r}")
            if any(ch in domain for ch in ("/", ":")):
                raise ValueError(f"Non-domain entry at line {lineno}: {domain!r}")

            labels = domain.split(".")
            if len(labels) < 2 or any(not label for label in labels):
                raise ValueError(f"Unsafe/invalid domain at line {lineno}: {domain!r}")

            try:
                ipaddress.ip_address(domain)
            except ValueError:
                pass
            else:
                raise ValueError(f"Unexpected IP in domain list at line {lineno}: {domain!r}")

            if domain in domains:
                duplicate_rows += 1
            else:
                domains.add(domain)

    if len(domains) < minimum:
        raise ValueError(
            f"Maltrail sanity check failed: {len(domains)} unique domains < minimum {minimum}"
        )

    return domains, raw_rows, duplicate_rows


def compact_domain_suffixes(domains: set[str]) -> tuple[list[str], int]:
    """Remove domain_suffix entries already covered by a source parent.

    This is suffix-trie-equivalent compaction without materialising a large
    Python trie: shortest domains are processed first and every candidate
    checks only its DNS-label parents in O(number_of_labels).
    """
    kept: set[str] = set()

    # Parent suffixes always have fewer labels, so they are guaranteed to be
    # in `kept` before a child is examined.
    for domain in sorted(domains, key=lambda item: (item.count("."), item)):
        labels = domain.split(".")
        redundant = any(".".join(labels[i:]) in kept for i in range(1, len(labels)))
        if not redundant:
            kept.add(domain)

    # Semantic-equivalence proof:
    # 1. Every retained suffix is an original source domain, so no broader
    #    parent is invented.
    # 2. Every original domain is covered by itself or by a retained parent
    #    on a DNS-label boundary.
    if not kept.issubset(domains):
        raise ValueError("Domain suffix compaction introduced a non-source suffix")

    for domain in domains:
        labels = domain.split(".")
        if not any(".".join(labels[i:]) in kept for i in range(0, len(labels))):
            raise ValueError(f"Domain suffix compaction lost coverage for {domain}")

    result = sorted(kept)
    return result, len(domains) - len(result)


# ============================================================
# Previous-build safety guard
# ============================================================


def load_previous_manifest(path: Path | None) -> dict | None:
    if path is None or not path.is_file() or path.stat().st_size == 0:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Unable to read previous manifest {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Previous manifest must contain a JSON object")
    return data


def guard_drop(name: str, new: int, old: int | None, max_drop_ratio: float, allow: bool) -> None:
    if old is None or old <= 0:
        return
    threshold = old * (1.0 - max_drop_ratio)
    if new < threshold:
        message = (
            f"{name} dropped from {old:,} to {new:,} "
            f"({(1 - new / old) * 100:.1f}% drop; allowed {max_drop_ratio * 100:.1f}%)"
        )
        if allow:
            print(f"WARNING: {message} -- explicitly allowed")
        else:
            raise ValueError(message)


# ============================================================
# sing-box
# ============================================================


def compile_ruleset(sing_box: Path, source: Path, output: Path) -> None:
    subprocess.run(
        [str(sing_box), "rule-set", "compile", str(source), "-o", str(output)],
        check=True,
    )

    if not output.is_file() or output.stat().st_size == 0:
        raise ValueError(f"Empty SRS output: {output}")

    # Verify that sing-box itself can read back the generated binary.
    with tempfile.TemporaryDirectory() as td:
        check_json = Path(td) / "check.json"
        subprocess.run(
            [str(sing_box), "rule-set", "decompile", str(output), "-o", str(check_json)],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        data = json.loads(check_json.read_text(encoding="utf-8"))
        if not isinstance(data.get("rules"), list):
            raise ValueError(f"Invalid decompiled rule-set: {output}")


# ============================================================
# Metadata / docs
# ============================================================


def make_readme(stats: dict, kind: str) -> str:
    ext = "txt" if kind == "text" else "srs"
    rows = []
    for level in range(1, 9):
        item = stats["ipsum"]["levels"][str(level)]
        original = item["source_unique_ips"]
        cidrs = item["published_entries"]
        reduction = 0.0 if original == 0 else (1 - cidrs / original) * 100
        rows.append(f"| {level} | {original:,} | {cidrs:,} | {reduction:.2f}% |")

    compiler_line = ""
    if kind == "srs":
        compiler_line = f"- sing-box compiler: `{stats['sources']['sing_box']['version']}`\n"

    file_lines = [
        f"- `ipsum-level-1.{ext}` ... `ipsum-level-8.{ext}`",
        f"- `maltrail-malware-domains.{ext}`",
    ]
    if kind == "text":
        file_lines.append(
            "- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)"
        )
    file_lines.append("- `manifest.json`")

    if kind == "text":
        compatibility = (
            "- `maltrail_ip.txt` -> `ipsum-level-1.txt`\n"
            "- `maltrail_domain.txt` -> exact de-duplicated "
            "`maltrail-malware-domains-full.txt` (legacy text compatibility)"
        )
    else:
        compatibility = (
            "- `maltrail_ip.srs` -> `ipsum-level-1.srs`\n"
            "- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`"
        )

    return f"""# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
{chr(10).join(rows)}

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: {stats['maltrail_malware_domains']['raw_rows']:,}
- Unique domains after exact de-duplication: {stats['maltrail_malware_domains']['unique_domains']:,}
- Exact duplicate rows removed: {stats['maltrail_malware_domains']['exact_duplicates_removed']:,}
- Redundant child suffixes removed: {stats['maltrail_malware_domains']['suffix_redundant_removed']:,}
- Published `domain_suffix` entries: {stats['maltrail_malware_domains']['published_domain_suffixes']:,}

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `{stats['sources']['ipsum']['commit']}`
- Maltrail Trails release: `{stats['sources']['maltrail_trails']['release']}`
{compiler_line}- sing-box source rule-set version: `{stats['ruleset_source_format_version']}`

## Files

{chr(10).join(file_lines)}

## Compatibility aliases

{compatibility}
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ipsum", type=Path, required=True)
    parser.add_argument("--domains", type=Path, required=True)
    parser.add_argument("--sing-box", type=Path, required=True)
    parser.add_argument("--text-dir", type=Path, required=True)
    parser.add_argument("--srs-dir", type=Path, required=True)
    parser.add_argument("--ipsum-repo", required=True)
    parser.add_argument("--ipsum-sha", required=True)
    parser.add_argument("--trails-repo", required=True)
    parser.add_argument("--trails-release", required=True)
    parser.add_argument("--trails-asset", required=True)
    parser.add_argument("--sing-box-version", required=True)
    parser.add_argument("--ruleset-version", type=int, default=2)
    parser.add_argument("--min-ipsum-unique", type=int, default=1000)
    parser.add_argument("--min-domains", type=int, default=1000)
    parser.add_argument("--previous-manifest", type=Path)
    parser.add_argument("--max-drop-ratio", type=float, default=0.50)
    parser.add_argument("--allow-large-drop", action="store_true")
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()

    if not 0.0 <= args.max_drop_ratio < 1.0:
        raise ValueError("--max-drop-ratio must be >= 0 and < 1")

    args.text_dir.mkdir(parents=True, exist_ok=True)
    args.srs_dir.mkdir(parents=True, exist_ok=True)

    previous = load_previous_manifest(args.previous_manifest)

    ip_counts, raw_ip_rows, duplicate_ip_rows = parse_ipsum(args.ipsum, args.min_ipsum_unique)
    domains, raw_domain_rows, duplicate_domain_rows = parse_domains(args.domains, args.min_domains)
    compact_domains, suffix_removed = compact_domain_suffixes(domains)

    old_ip_count = None
    old_domain_count = None
    old_published_domains = None
    if previous:
        old_ip_count = previous.get("ipsum", {}).get("unique_ips")
        old_domain_count = previous.get("maltrail_malware_domains", {}).get("unique_domains")
        old_published_domains = previous.get("maltrail_malware_domains", {}).get(
            "published_domain_suffixes"
        )

    guard_drop(
        "IPsum unique IP count",
        len(ip_counts),
        old_ip_count,
        args.max_drop_ratio,
        args.allow_large_drop,
    )
    guard_drop(
        "Maltrail unique domain count",
        len(domains),
        old_domain_count,
        args.max_drop_ratio,
        args.allow_large_drop,
    )
    guard_drop(
        "Maltrail published suffix count",
        len(compact_domains),
        old_published_domains,
        args.max_drop_ratio,
        args.allow_large_drop,
    )

    levels: dict[str, dict] = {}
    previous_members: set[IPAddress] | None = None

    with tempfile.TemporaryDirectory() as td:
        source_dir = Path(td)

        for level in range(1, 9):
            members = {ip for ip, count in ip_counts.items() if count >= level}

            if previous_members is not None and not members.issubset(previous_members):
                raise ValueError(f"IPsum hierarchy check failed at level {level}")
            previous_members = members

            collapsed = exact_collapse(members)
            entries = [format_network(network) for network in collapsed]

            text_file = args.text_dir / f"ipsum-level-{level}.txt"
            write_lines(text_file, entries)

            source_file = source_dir / f"ipsum-level-{level}.json"
            write_json(
                source_file,
                {
                    "version": args.ruleset_version,
                    "rules": [{"ip_cidr": entries}] if entries else [],
                },
            )

            srs_file = args.srs_dir / f"ipsum-level-{level}.srs"
            compile_ruleset(args.sing_box, source_file, srs_file)

            levels[str(level)] = {
                "source_unique_ips": len(members),
                "published_entries": len(entries),
                "represented_ips": sum(network.num_addresses for network in collapsed),
                "text_file": text_file.name,
                "text_size": text_file.stat().st_size,
                "text_sha256": sha256_file(text_file),
                "srs_file": srs_file.name,
                "srs_size": srs_file.stat().st_size,
                "srs_sha256": sha256_file(srs_file),
            }

        # Canonical effective suffix list: exact duplicates + redundant child
        # suffixes removed. This list maps 1:1 to SRS domain_suffix semantics.
        domain_text = args.text_dir / "maltrail-malware-domains.txt"
        write_lines(domain_text, compact_domains)

        # Preserve the exact de-duplicated IOC inventory separately for audit
        # and exact-domain consumers, where suffix compaction would not be
        # semantically equivalent.
        domain_full_text = args.text_dir / "maltrail-malware-domains-full.txt"
        write_lines(domain_full_text, sorted(domains))

        domain_source = source_dir / "maltrail-malware-domains.json"
        write_json(
            domain_source,
            {
                "version": args.ruleset_version,
                "rules": [{"domain_suffix": compact_domains}],
            },
        )

        domain_srs = args.srs_dir / "maltrail-malware-domains.srs"
        compile_ruleset(args.sing_box, domain_source, domain_srs)

    stats = {
        "ruleset_source_format_version": args.ruleset_version,
        "sources": {
            "ipsum": {
                "repository": args.ipsum_repo,
                "commit": args.ipsum_sha,
                "upstream_sha256": sha256_file(args.ipsum),
            },
            "maltrail_trails": {
                "repository": args.trails_repo,
                "release": args.trails_release,
                "asset": args.trails_asset,
                "upstream_sha256": sha256_file(args.domains),
            },
            "sing_box": {"version": args.sing_box_version},
        },
        "ipsum": {
            "raw_rows": raw_ip_rows,
            "unique_ips": len(ip_counts),
            "exact_duplicates_removed": duplicate_ip_rows,
            "levels": levels,
        },
        "maltrail_malware_domains": {
            "raw_rows": raw_domain_rows,
            "unique_domains": len(domains),
            "exact_duplicates_removed": duplicate_domain_rows,
            "suffix_redundant_removed": suffix_removed,
            "published_domain_suffixes": len(compact_domains),
            "text_file": domain_text.name,
            "text_size": domain_text.stat().st_size,
            "text_sha256": sha256_file(domain_text),
            "full_text_file": domain_full_text.name,
            "full_text_size": domain_full_text.stat().st_size,
            "full_text_sha256": sha256_file(domain_full_text),
            "srs_file": domain_srs.name,
            "srs_size": domain_srs.stat().st_size,
            "srs_sha256": sha256_file(domain_srs),
        },
    }

    # Compatibility aliases for existing consumers.
    (args.text_dir / "maltrail_ip.txt").write_bytes(
        (args.text_dir / "ipsum-level-1.txt").read_bytes()
    )
    (args.srs_dir / "maltrail_ip.srs").write_bytes(
        (args.srs_dir / "ipsum-level-1.srs").read_bytes()
    )
    # Keep the legacy text path exact-domain compatible with the old feed.
    (args.text_dir / "maltrail_domain.txt").write_bytes(domain_full_text.read_bytes())
    (args.srs_dir / "maltrail_domain.srs").write_bytes(domain_srs.read_bytes())

    # The text branch intentionally omits compiler/SRS metadata so a compiler
    # upgrade alone does not dirty the text branch.
    text_manifest = copy.deepcopy(stats)
    text_manifest["sources"].pop("sing_box", None)
    for item in text_manifest["ipsum"]["levels"].values():
        item.pop("srs_file", None)
        item.pop("srs_size", None)
        item.pop("srs_sha256", None)
    for key in ("srs_file", "srs_size", "srs_sha256"):
        text_manifest["maltrail_malware_domains"].pop(key, None)

    srs_manifest = copy.deepcopy(stats)
    for key in ("full_text_file", "full_text_size", "full_text_sha256"):
        srs_manifest["maltrail_malware_domains"].pop(key, None)

    write_json(args.text_dir / "manifest.json", text_manifest)
    write_json(args.srs_dir / "manifest.json", srs_manifest)

    (args.text_dir / "README.md").write_text(
        make_readme(stats, "text"), encoding="utf-8", newline="\n"
    )
    (args.srs_dir / "README.md").write_text(
        make_readme(stats, "srs"), encoding="utf-8", newline="\n"
    )

    if args.summary:
        summary = [
            "## Security rule-set build",
            "",
            f"- IPsum commit: `{args.ipsum_sha}`",
            f"- Maltrail Trails release: `{args.trails_release}`",
            f"- sing-box compiler: `{args.sing_box_version}`",
            "",
            "### IPsum",
            "",
            "| Level | Unique IPs | IP/CIDR entries | Reduction | TXT | SRS |",
            "|---:|---:|---:|---:|---:|---:|",
        ]

        for level in range(1, 9):
            item = levels[str(level)]
            original = item["source_unique_ips"]
            entries = item["published_entries"]
            reduction = 0.0 if original == 0 else (1 - entries / original) * 100
            summary.append(
                f"| {level} | {original:,} | {entries:,} | {reduction:.2f}% "
                f"| {human_bytes(item['text_size'])} | {human_bytes(item['srs_size'])} |"
            )

        summary += [
            "",
            "### Maltrail malware domains",
            "",
            f"- Raw rows: {raw_domain_rows:,}",
            f"- Unique after exact de-duplication: {len(domains):,}",
            f"- Exact duplicate rows removed: {duplicate_domain_rows:,}",
            f"- Redundant child suffixes removed: {suffix_removed:,}",
            f"- Published domain_suffix entries: {len(compact_domains):,}",
            f"- Compacted TXT size: {human_bytes(domain_text.stat().st_size)}",
            f"- Exact full TXT size: {human_bytes(domain_full_text.stat().st_size)}",
            f"- SRS size: {human_bytes(domain_srs.stat().st_size)}",
        ]

        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text("\n".join(summary) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
