# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 118,954 | 88,047 | 25.98% |
| 2 | 34,770 | 24,990 | 28.13% |
| 3 | 18,526 | 12,939 | 30.16% |
| 4 | 9,947 | 7,507 | 24.53% |
| 5 | 4,798 | 4,068 | 15.21% |
| 6 | 1,975 | 1,736 | 12.10% |
| 7 | 643 | 568 | 11.66% |
| 8 | 130 | 117 | 10.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,037,359
- Unique domains after exact de-duplication: 1,037,359
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,480
- Published `domain_suffix` entries: 893,879

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `31ea73dc5b1afafdda1ff681b337957e9fb049ba`
- Maltrail Trails release: `content-20261009-2316`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
