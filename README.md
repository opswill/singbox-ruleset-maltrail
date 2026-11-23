# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 140,895 | 98,859 | 29.83% |
| 2 | 39,324 | 29,088 | 26.03% |
| 3 | 17,900 | 13,207 | 26.22% |
| 4 | 8,261 | 6,373 | 22.85% |
| 5 | 2,609 | 2,230 | 14.53% |
| 6 | 633 | 585 | 7.58% |
| 7 | 134 | 128 | 4.48% |
| 8 | 32 | 32 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,149,198
- Unique domains after exact de-duplication: 1,149,198
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 171,528
- Published `domain_suffix` entries: 977,670

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `8bdfb69fabb0a3edb7152bcda452a50c79a6fa08`
- Maltrail Trails release: `content-20261122-2022`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
