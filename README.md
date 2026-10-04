# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 109,695 | 80,253 | 26.84% |
| 2 | 32,377 | 23,140 | 28.53% |
| 3 | 16,495 | 11,521 | 30.15% |
| 4 | 8,845 | 6,540 | 26.06% |
| 5 | 3,731 | 2,927 | 21.55% |
| 6 | 1,262 | 1,031 | 18.30% |
| 7 | 311 | 277 | 10.93% |
| 8 | 44 | 41 | 6.82% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,012,976
- Unique domains after exact de-duplication: 1,012,976
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,179
- Published `domain_suffix` entries: 869,797

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `53df81002334613f7d1f0ff87d9b2049ec6117b6`
- Maltrail Trails release: `content-20261003-2208`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
