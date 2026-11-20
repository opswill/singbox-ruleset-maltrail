# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 141,785 | 100,723 | 28.96% |
| 2 | 41,548 | 30,385 | 26.87% |
| 3 | 19,089 | 14,096 | 26.16% |
| 4 | 9,023 | 6,966 | 22.80% |
| 5 | 3,151 | 2,738 | 13.11% |
| 6 | 812 | 747 | 8.00% |
| 7 | 175 | 169 | 3.43% |
| 8 | 42 | 42 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,145,845
- Unique domains after exact de-duplication: 1,145,845
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 170,987
- Published `domain_suffix` entries: 974,858

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `64cb46d9a52d26b3e33928d274c9d05d9aa924dd`
- Maltrail Trails release: `content-20261119-2135`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
