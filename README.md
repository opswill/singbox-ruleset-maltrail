# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 136,536 | 96,765 | 29.13% |
| 2 | 34,706 | 24,337 | 29.88% |
| 3 | 18,595 | 12,824 | 31.04% |
| 4 | 9,751 | 7,186 | 26.30% |
| 5 | 4,268 | 3,568 | 16.40% |
| 6 | 1,312 | 1,221 | 6.94% |
| 7 | 305 | 291 | 4.59% |
| 8 | 61 | 60 | 1.64% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,089,295
- Unique domains after exact de-duplication: 1,089,295
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 150,990
- Published `domain_suffix` entries: 938,305

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `4dda1b57ff65a9fe7ffa91913b63256ab1c4b453`
- Maltrail Trails release: `content-20261104-2026`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
