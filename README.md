# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 126,930 | 92,839 | 26.86% |
| 2 | 34,912 | 25,071 | 28.19% |
| 3 | 18,721 | 13,344 | 28.72% |
| 4 | 10,073 | 7,786 | 22.70% |
| 5 | 4,558 | 3,936 | 13.65% |
| 6 | 1,862 | 1,618 | 13.10% |
| 7 | 629 | 553 | 12.08% |
| 8 | 120 | 116 | 3.33% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,047,040
- Unique domains after exact de-duplication: 1,047,040
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 144,207
- Published `domain_suffix` entries: 902,833

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `01a340f74a6b6ddce41ea1c74ef6fabb8d49411d`
- Maltrail Trails release: `content-20261014-1801`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
