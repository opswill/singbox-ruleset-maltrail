# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 139,571 | 98,075 | 29.73% |
| 2 | 35,107 | 25,295 | 27.95% |
| 3 | 18,001 | 12,458 | 30.79% |
| 4 | 9,634 | 7,069 | 26.62% |
| 5 | 4,456 | 3,733 | 16.23% |
| 6 | 1,516 | 1,415 | 6.66% |
| 7 | 286 | 264 | 7.69% |
| 8 | 53 | 44 | 16.98% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,086,903
- Unique domains after exact de-duplication: 1,086,903
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 150,100
- Published `domain_suffix` entries: 936,803

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `e6f0f90246bdae3ef69f59049c3133286ac6b58a`
- Maltrail Trails release: `content-20261102-2219`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
