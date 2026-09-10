# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 125,551 | 96,795 | 22.90% |
| 2 | 32,623 | 24,868 | 23.77% |
| 3 | 17,667 | 13,402 | 24.14% |
| 4 | 8,806 | 7,146 | 18.85% |
| 5 | 3,889 | 3,327 | 14.45% |
| 6 | 1,353 | 1,139 | 15.82% |
| 7 | 417 | 345 | 17.27% |
| 8 | 134 | 128 | 4.48% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 973,818
- Unique domains after exact de-duplication: 973,818
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,087
- Published `domain_suffix` entries: 834,731

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `6c9059d56e65c55f0bc37afa1dca977e91e86f17`
- Maltrail Trails release: `content-20260909-2142`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
