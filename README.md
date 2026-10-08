# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 115,850 | 86,957 | 24.94% |
| 2 | 33,383 | 24,663 | 26.12% |
| 3 | 17,372 | 12,930 | 25.57% |
| 4 | 8,917 | 7,289 | 18.26% |
| 5 | 3,385 | 2,884 | 14.80% |
| 6 | 1,068 | 896 | 16.10% |
| 7 | 305 | 260 | 14.75% |
| 8 | 68 | 67 | 1.47% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,034,701
- Unique domains after exact de-duplication: 1,034,701
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,377
- Published `domain_suffix` entries: 891,324

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `2d660d93fcc957ab936948060b7664ee24b722f5`
- Maltrail Trails release: `content-20261007-2335`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
