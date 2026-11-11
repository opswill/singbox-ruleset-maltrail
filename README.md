# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 133,200 | 92,878 | 30.27% |
| 2 | 33,645 | 24,790 | 26.32% |
| 3 | 17,172 | 12,768 | 25.65% |
| 4 | 8,105 | 6,252 | 22.86% |
| 5 | 3,423 | 3,014 | 11.95% |
| 6 | 977 | 918 | 6.04% |
| 7 | 224 | 218 | 2.68% |
| 8 | 44 | 44 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,095,669
- Unique domains after exact de-duplication: 1,095,669
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 152,815
- Published `domain_suffix` entries: 942,854

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `38d7397825dc34fe9759cd804f9191b0a17b0363`
- Maltrail Trails release: `content-20261110-2028`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
