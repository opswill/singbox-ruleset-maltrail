# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 129,849 | 98,402 | 24.22% |
| 2 | 36,218 | 27,641 | 23.68% |
| 3 | 20,677 | 15,476 | 25.15% |
| 4 | 11,921 | 9,119 | 23.50% |
| 5 | 6,371 | 5,106 | 19.86% |
| 6 | 2,675 | 2,151 | 19.59% |
| 7 | 844 | 642 | 23.93% |
| 8 | 232 | 194 | 16.38% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 990,630
- Unique domains after exact de-duplication: 990,630
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,002
- Published `domain_suffix` entries: 850,628

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `7b2d82fa6bdf9ecb15e0753f5c450d1942c079e0`
- Maltrail Trails release: `content-20260919-1630`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
