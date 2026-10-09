# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 118,773 | 90,293 | 23.98% |
| 2 | 34,669 | 25,440 | 26.62% |
| 3 | 18,262 | 13,161 | 27.93% |
| 4 | 9,851 | 7,764 | 21.19% |
| 5 | 4,686 | 4,048 | 13.62% |
| 6 | 1,813 | 1,604 | 11.53% |
| 7 | 567 | 505 | 10.93% |
| 8 | 129 | 119 | 7.75% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,036,182
- Unique domains after exact de-duplication: 1,036,182
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,466
- Published `domain_suffix` entries: 892,716

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `0a19d9621881dfffa1f60cd3a59f533bbd59adcd`
- Maltrail Trails release: `content-20261008-2346`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
