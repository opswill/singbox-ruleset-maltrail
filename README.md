# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 144,310 | 104,563 | 27.54% |
| 2 | 34,766 | 25,229 | 27.43% |
| 3 | 18,433 | 12,879 | 30.13% |
| 4 | 9,666 | 7,106 | 26.48% |
| 5 | 4,471 | 3,830 | 14.34% |
| 6 | 1,435 | 1,327 | 7.53% |
| 7 | 342 | 324 | 5.26% |
| 8 | 70 | 69 | 1.43% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,092,564
- Unique domains after exact de-duplication: 1,092,564
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 151,933
- Published `domain_suffix` entries: 940,631

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `2bee9ac4c4e96164428ff40faeafd09b6819742b`
- Maltrail Trails release: `content-20261106-1957`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
