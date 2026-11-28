# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 146,370 | 102,409 | 30.03% |
| 2 | 39,712 | 28,861 | 27.32% |
| 3 | 17,845 | 13,020 | 27.04% |
| 4 | 8,430 | 6,550 | 22.30% |
| 5 | 3,084 | 2,714 | 12.00% |
| 6 | 915 | 873 | 4.59% |
| 7 | 194 | 191 | 1.55% |
| 8 | 42 | 41 | 2.38% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,156,493
- Unique domains after exact de-duplication: 1,156,493
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 173,206
- Published `domain_suffix` entries: 983,287

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `7cdb123f5390e363ec759d400d36ae06176b7ce0`
- Maltrail Trails release: `content-20261127-2158`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
