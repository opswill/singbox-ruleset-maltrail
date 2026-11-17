# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 135,530 | 95,951 | 29.20% |
| 2 | 37,645 | 27,455 | 27.07% |
| 3 | 17,608 | 13,351 | 24.18% |
| 4 | 8,073 | 6,409 | 20.61% |
| 5 | 2,802 | 2,471 | 11.81% |
| 6 | 794 | 757 | 4.66% |
| 7 | 205 | 195 | 4.88% |
| 8 | 48 | 45 | 6.25% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,140,975
- Unique domains after exact de-duplication: 1,140,975
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 170,024
- Published `domain_suffix` entries: 970,951

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `44e4141b8e941fc3d2ec952c28cad4b38537fdc5`
- Maltrail Trails release: `content-20261116-2254`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
