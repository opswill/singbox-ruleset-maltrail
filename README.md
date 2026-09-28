# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 115,711 | 86,688 | 25.08% |
| 2 | 34,928 | 26,451 | 24.27% |
| 3 | 18,758 | 14,028 | 25.22% |
| 4 | 10,093 | 7,891 | 21.82% |
| 5 | 5,109 | 4,260 | 16.62% |
| 6 | 2,072 | 1,771 | 14.53% |
| 7 | 666 | 583 | 12.46% |
| 8 | 162 | 150 | 7.41% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,004,661
- Unique domains after exact de-duplication: 1,004,661
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 142,580
- Published `domain_suffix` entries: 862,081

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `cbac19c78e284a6bdf1aca33bb9e90496b3c3927`
- Maltrail Trails release: `content-20260927-2212`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
