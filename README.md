# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 142,959 | 102,907 | 28.02% |
| 2 | 35,261 | 25,036 | 29.00% |
| 3 | 18,185 | 12,551 | 30.98% |
| 4 | 10,033 | 7,312 | 27.12% |
| 5 | 4,654 | 3,973 | 14.63% |
| 6 | 1,449 | 1,345 | 7.18% |
| 7 | 322 | 312 | 3.11% |
| 8 | 62 | 62 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,089,699
- Unique domains after exact de-duplication: 1,089,699
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 151,069
- Published `domain_suffix` entries: 938,630

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `0abf5eb303c82c8961e05ff6fa23cbb7b6356ac1`
- Maltrail Trails release: `content-20261105-2040`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
