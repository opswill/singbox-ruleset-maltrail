# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 119,353 | 86,332 | 27.67% |
| 2 | 34,573 | 24,810 | 28.24% |
| 3 | 18,903 | 13,431 | 28.95% |
| 4 | 10,116 | 7,866 | 22.24% |
| 5 | 4,723 | 4,059 | 14.06% |
| 6 | 1,898 | 1,658 | 12.64% |
| 7 | 609 | 521 | 14.45% |
| 8 | 138 | 132 | 4.35% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,044,434
- Unique domains after exact de-duplication: 1,044,434
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,767
- Published `domain_suffix` entries: 900,667

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `10f0e0ea98c94363a7f3fcc538acf181d3d37fa4`
- Maltrail Trails release: `content-20261011-2255`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
