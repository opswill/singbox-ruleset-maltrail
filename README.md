# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 139,424 | 99,542 | 28.60% |
| 2 | 41,301 | 30,692 | 25.69% |
| 3 | 19,549 | 14,667 | 24.97% |
| 4 | 8,439 | 6,896 | 18.28% |
| 5 | 2,855 | 2,519 | 11.77% |
| 6 | 732 | 659 | 9.97% |
| 7 | 175 | 166 | 5.14% |
| 8 | 30 | 30 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,146,934
- Unique domains after exact de-duplication: 1,146,934
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 171,079
- Published `domain_suffix` entries: 975,855

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `32dde9709d32a37740d79a63cffd2bfb7cd701e1`
- Maltrail Trails release: `content-20261120-2105`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
