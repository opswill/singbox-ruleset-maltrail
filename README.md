# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 123,241 | 89,173 | 27.64% |
| 2 | 34,473 | 24,524 | 28.86% |
| 3 | 18,892 | 13,084 | 30.74% |
| 4 | 9,772 | 7,289 | 25.41% |
| 5 | 4,416 | 3,760 | 14.86% |
| 6 | 1,576 | 1,435 | 8.95% |
| 7 | 370 | 353 | 4.59% |
| 8 | 62 | 62 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,052,392
- Unique domains after exact de-duplication: 1,052,392
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 144,289
- Published `domain_suffix` entries: 908,103

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `6e8e346e33aea608f0bdcc94552e4c1d3c20068f`
- Maltrail Trails release: `content-20261015-2220`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
