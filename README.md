# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 131,962 | 102,696 | 22.18% |
| 2 | 31,923 | 24,595 | 22.96% |
| 3 | 16,086 | 12,711 | 20.98% |
| 4 | 7,558 | 6,394 | 15.40% |
| 5 | 3,325 | 2,894 | 12.96% |
| 6 | 1,182 | 1,002 | 15.23% |
| 7 | 384 | 321 | 16.41% |
| 8 | 116 | 99 | 14.66% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 972,396
- Unique domains after exact de-duplication: 972,396
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 138,849
- Published `domain_suffix` entries: 833,547

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `c0e606e6a12c9e08c1708422f790884a4046c1fd`
- Maltrail Trails release: `content-20260908-2152`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
