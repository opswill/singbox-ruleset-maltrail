# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 139,878 | 99,708 | 28.72% |
| 2 | 33,573 | 24,421 | 27.26% |
| 3 | 17,509 | 12,525 | 28.47% |
| 4 | 8,680 | 6,698 | 22.83% |
| 5 | 3,847 | 3,399 | 11.65% |
| 6 | 1,167 | 1,105 | 5.31% |
| 7 | 273 | 268 | 1.83% |
| 8 | 53 | 53 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,095,061
- Unique domains after exact de-duplication: 1,095,061
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 152,740
- Published `domain_suffix` entries: 942,321

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `1cb737314820334991982fe76d4c0861a4156e96`
- Maltrail Trails release: `content-20261108-2254`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
