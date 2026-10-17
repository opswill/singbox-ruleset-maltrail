# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 125,469 | 90,936 | 27.52% |
| 2 | 33,971 | 24,023 | 29.28% |
| 3 | 18,347 | 12,559 | 31.55% |
| 4 | 9,653 | 7,172 | 25.70% |
| 5 | 4,457 | 3,851 | 13.60% |
| 6 | 1,627 | 1,485 | 8.73% |
| 7 | 441 | 417 | 5.44% |
| 8 | 68 | 68 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,053,118
- Unique domains after exact de-duplication: 1,053,118
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 144,313
- Published `domain_suffix` entries: 908,805

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `cb3b3dc24986358a2092d359a7f812acb9c9a773`
- Maltrail Trails release: `content-20261016-2206`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
