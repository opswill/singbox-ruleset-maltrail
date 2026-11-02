# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 139,773 | 101,302 | 27.52% |
| 2 | 36,666 | 26,410 | 27.97% |
| 3 | 18,258 | 12,646 | 30.74% |
| 4 | 9,639 | 7,151 | 25.81% |
| 5 | 4,662 | 3,979 | 14.65% |
| 6 | 1,793 | 1,687 | 5.91% |
| 7 | 500 | 477 | 4.60% |
| 8 | 76 | 72 | 5.26% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,086,257
- Unique domains after exact de-duplication: 1,086,257
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,776
- Published `domain_suffix` entries: 936,481

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `27783b594dadead4d0f564de8163bb37e35480c1`
- Maltrail Trails release: `content-20261101-1826`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
