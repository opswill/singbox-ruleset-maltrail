# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 122,565 | 93,264 | 23.91% |
| 2 | 33,458 | 25,801 | 22.89% |
| 3 | 16,772 | 13,062 | 22.12% |
| 4 | 8,261 | 6,659 | 19.39% |
| 5 | 4,117 | 3,410 | 17.17% |
| 6 | 1,724 | 1,409 | 18.27% |
| 7 | 593 | 490 | 17.37% |
| 8 | 166 | 150 | 9.64% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 989,357
- Unique domains after exact de-duplication: 989,357
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,527
- Published `domain_suffix` entries: 849,830

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `d1de48fae2ad63cb854c9fcf9bf75a2544f07ee1`
- Maltrail Trails release: `content-20260916-2211`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
