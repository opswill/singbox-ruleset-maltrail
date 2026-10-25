# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 128,244 | 95,991 | 25.15% |
| 2 | 36,497 | 26,649 | 26.98% |
| 3 | 19,670 | 14,269 | 27.46% |
| 4 | 10,858 | 8,560 | 21.16% |
| 5 | 5,289 | 4,564 | 13.71% |
| 6 | 2,035 | 1,851 | 9.04% |
| 7 | 545 | 509 | 6.61% |
| 8 | 102 | 98 | 3.92% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,067,852
- Unique domains after exact de-duplication: 1,067,852
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 146,801
- Published `domain_suffix` entries: 921,051

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `ae08b70f8b9a7000503c8ca304da40c108ae26c2`
- Maltrail Trails release: `content-20261024-2137`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
