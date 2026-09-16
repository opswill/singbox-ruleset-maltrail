# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 118,113 | 90,589 | 23.30% |
| 2 | 32,142 | 24,417 | 24.03% |
| 3 | 16,604 | 12,822 | 22.78% |
| 4 | 7,974 | 6,528 | 18.13% |
| 5 | 2,865 | 2,237 | 21.92% |
| 6 | 1,076 | 829 | 22.96% |
| 7 | 388 | 296 | 23.71% |
| 8 | 74 | 71 | 4.05% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 984,796
- Unique domains after exact de-duplication: 984,796
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,489
- Published `domain_suffix` entries: 845,307

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `edcc22a3318e4965a95667abcc35f9b3644dd4d3`
- Maltrail Trails release: `content-20260915-2214`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
