# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 108,749 | 80,602 | 25.88% |
| 2 | 32,182 | 23,074 | 28.30% |
| 3 | 16,661 | 11,569 | 30.56% |
| 4 | 8,972 | 6,857 | 23.57% |
| 5 | 3,528 | 2,864 | 18.82% |
| 6 | 899 | 751 | 16.46% |
| 7 | 186 | 171 | 8.06% |
| 8 | 20 | 20 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,012,381
- Unique domains after exact de-duplication: 1,012,381
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,067
- Published `domain_suffix` entries: 869,314

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `51ea58108deea0d796956ead5a02d3c220791144`
- Maltrail Trails release: `content-20261002-2258`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
