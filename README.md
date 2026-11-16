# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 135,040 | 93,427 | 30.82% |
| 2 | 38,088 | 27,252 | 28.45% |
| 3 | 17,732 | 12,798 | 27.83% |
| 4 | 8,446 | 6,609 | 21.75% |
| 5 | 2,773 | 2,416 | 12.87% |
| 6 | 667 | 621 | 6.90% |
| 7 | 156 | 149 | 4.49% |
| 8 | 35 | 34 | 2.86% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,119,786
- Unique domains after exact de-duplication: 1,119,786
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 157,672
- Published `domain_suffix` entries: 962,114

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `7a8f54a4bd4671fb692ce1dbd650a65521cdee95`
- Maltrail Trails release: `content-20261115-1923`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
