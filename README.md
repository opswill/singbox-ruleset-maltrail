# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 115,156 | 86,626 | 24.78% |
| 2 | 34,352 | 26,108 | 24.00% |
| 3 | 18,503 | 14,011 | 24.28% |
| 4 | 9,830 | 7,863 | 20.01% |
| 5 | 4,856 | 4,152 | 14.50% |
| 6 | 2,039 | 1,762 | 13.59% |
| 7 | 673 | 598 | 11.14% |
| 8 | 164 | 153 | 6.71% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,003,320
- Unique domains after exact de-duplication: 1,003,320
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 142,484
- Published `domain_suffix` entries: 860,836

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `77e0ae2cd444bb283ac7ee12bcac40008202b2da`
- Maltrail Trails release: `content-20260926-2158`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
