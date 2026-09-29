# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 121,838 | 92,084 | 24.42% |
| 2 | 34,475 | 26,229 | 23.92% |
| 3 | 17,604 | 13,667 | 22.36% |
| 4 | 8,613 | 7,070 | 17.91% |
| 5 | 4,242 | 3,708 | 12.59% |
| 6 | 1,625 | 1,477 | 9.11% |
| 7 | 408 | 375 | 8.09% |
| 8 | 86 | 80 | 6.98% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,005,203
- Unique domains after exact de-duplication: 1,005,203
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 142,598
- Published `domain_suffix` entries: 862,605

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `2ff919e1d3a6f2434eed695c1a0b5ee9d1cf79a7`
- Maltrail Trails release: `content-20260928-2349`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
