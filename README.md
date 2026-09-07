# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 132,013 | 102,158 | 22.62% |
| 2 | 33,753 | 26,213 | 22.34% |
| 3 | 16,196 | 12,857 | 20.62% |
| 4 | 7,146 | 6,141 | 14.06% |
| 5 | 3,200 | 2,862 | 10.56% |
| 6 | 909 | 785 | 13.64% |
| 7 | 261 | 211 | 19.16% |
| 8 | 59 | 54 | 8.47% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 970,935
- Unique domains after exact de-duplication: 970,935
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 138,685
- Published `domain_suffix` entries: 832,250

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `6fa1320f961fa026c2b2b5f71f3050af66311104`
- Maltrail Trails release: `content-20260906-1618`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
