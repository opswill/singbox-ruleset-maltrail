# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 136,343 | 93,338 | 31.54% |
| 2 | 39,541 | 28,481 | 27.97% |
| 3 | 18,337 | 13,473 | 26.53% |
| 4 | 8,515 | 6,821 | 19.89% |
| 5 | 3,322 | 3,038 | 8.55% |
| 6 | 854 | 825 | 3.40% |
| 7 | 140 | 139 | 0.71% |
| 8 | 23 | 23 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,119,175
- Unique domains after exact de-duplication: 1,119,175
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 157,606
- Published `domain_suffix` entries: 961,569

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `f7e547d316b858fa6bc0f39dfb154499005cbcf5`
- Maltrail Trails release: `content-20261113-2029`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
