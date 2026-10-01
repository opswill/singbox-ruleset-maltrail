# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 121,547 | 90,232 | 25.76% |
| 2 | 34,355 | 25,450 | 25.92% |
| 3 | 17,333 | 13,000 | 25.00% |
| 4 | 8,396 | 6,698 | 20.22% |
| 5 | 4,072 | 3,539 | 13.09% |
| 6 | 1,454 | 1,273 | 12.45% |
| 7 | 331 | 297 | 10.27% |
| 8 | 74 | 67 | 9.46% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,007,750
- Unique domains after exact de-duplication: 1,007,750
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 142,978
- Published `domain_suffix` entries: 864,772

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `3199cb75ba3d21adb9d4ac78bb05aaced55c7779`
- Maltrail Trails release: `content-20260930-2301`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
