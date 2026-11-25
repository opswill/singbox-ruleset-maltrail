# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 142,311 | 100,726 | 29.22% |
| 2 | 39,019 | 29,046 | 25.56% |
| 3 | 17,537 | 13,549 | 22.74% |
| 4 | 8,224 | 6,708 | 18.43% |
| 5 | 2,966 | 2,701 | 8.93% |
| 6 | 872 | 840 | 3.67% |
| 7 | 155 | 151 | 2.58% |
| 8 | 24 | 24 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,149,636
- Unique domains after exact de-duplication: 1,149,636
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 171,565
- Published `domain_suffix` entries: 978,071

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `79eadc9c2966b3f02c1ba3df983333a135cf973f`
- Maltrail Trails release: `content-20261124-2301`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
