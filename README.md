# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 129,399 | 99,511 | 23.10% |
| 2 | 35,545 | 27,081 | 23.81% |
| 3 | 19,040 | 14,354 | 24.61% |
| 4 | 9,918 | 7,820 | 21.15% |
| 5 | 5,065 | 4,190 | 17.28% |
| 6 | 2,122 | 1,761 | 17.01% |
| 7 | 660 | 554 | 16.06% |
| 8 | 174 | 156 | 10.34% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 999,105
- Unique domains after exact de-duplication: 999,105
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,459
- Published `domain_suffix` entries: 858,646

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `ae992521ad1bab29ff2fd60d91ba048815b2fcb5`
- Maltrail Trails release: `content-20260925-2221`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
