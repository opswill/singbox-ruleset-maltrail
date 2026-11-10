# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 130,398 | 90,331 | 30.73% |
| 2 | 33,481 | 24,862 | 25.74% |
| 3 | 17,226 | 12,796 | 25.72% |
| 4 | 8,304 | 6,339 | 23.66% |
| 5 | 3,552 | 3,104 | 12.61% |
| 6 | 1,013 | 958 | 5.43% |
| 7 | 226 | 222 | 1.77% |
| 8 | 54 | 53 | 1.85% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,095,355
- Unique domains after exact de-duplication: 1,095,355
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 152,758
- Published `domain_suffix` entries: 942,597

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `eb21f74e685af80ff9d1f3fb08bef1d80d0740c0`
- Maltrail Trails release: `content-20261109-2259`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
