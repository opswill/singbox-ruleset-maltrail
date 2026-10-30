# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 143,409 | 102,348 | 28.63% |
| 2 | 35,924 | 25,960 | 27.74% |
| 3 | 18,482 | 12,601 | 31.82% |
| 4 | 9,992 | 7,006 | 29.88% |
| 5 | 5,012 | 4,102 | 18.16% |
| 6 | 1,908 | 1,713 | 10.22% |
| 7 | 499 | 465 | 6.81% |
| 8 | 109 | 101 | 7.34% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,085,934
- Unique domains after exact de-duplication: 1,085,934
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,714
- Published `domain_suffix` entries: 936,220

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `b7fb9730a080144c695d3883d28d080447f0577c`
- Maltrail Trails release: `content-20261029-2318`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
