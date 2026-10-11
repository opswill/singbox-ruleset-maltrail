# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 116,723 | 86,279 | 26.08% |
| 2 | 34,592 | 25,161 | 27.26% |
| 3 | 18,834 | 13,726 | 27.12% |
| 4 | 9,670 | 7,763 | 19.72% |
| 5 | 4,518 | 3,935 | 12.90% |
| 6 | 1,776 | 1,571 | 11.54% |
| 7 | 598 | 515 | 13.88% |
| 8 | 136 | 117 | 13.97% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,037,625
- Unique domains after exact de-duplication: 1,037,625
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,599
- Published `domain_suffix` entries: 894,026

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `b8e415a2b589b2f14c19bfe80c17dfc0534c1e30`
- Maltrail Trails release: `content-20261010-2233`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
