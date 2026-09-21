# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 130,964 | 101,787 | 22.28% |
| 2 | 36,328 | 28,053 | 22.78% |
| 3 | 21,127 | 16,150 | 23.56% |
| 4 | 12,013 | 9,364 | 22.05% |
| 5 | 6,191 | 5,054 | 18.37% |
| 6 | 2,551 | 2,081 | 18.42% |
| 7 | 839 | 674 | 19.67% |
| 8 | 195 | 176 | 9.74% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 991,315
- Unique domains after exact de-duplication: 991,315
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,066
- Published `domain_suffix` entries: 851,249

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `ab55c9a9727417d5c0d6eb91ccf4d8730141452f`
- Maltrail Trails release: `content-20260920-2134`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
