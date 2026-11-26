# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 141,565 | 98,592 | 30.36% |
| 2 | 38,755 | 28,285 | 27.02% |
| 3 | 17,554 | 12,600 | 28.22% |
| 4 | 8,545 | 6,493 | 24.01% |
| 5 | 3,000 | 2,643 | 11.90% |
| 6 | 795 | 759 | 4.53% |
| 7 | 140 | 139 | 0.71% |
| 8 | 19 | 19 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,155,041
- Unique domains after exact de-duplication: 1,155,041
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 173,105
- Published `domain_suffix` entries: 981,936

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `ab940d09dbae981e2848ab1f890e85bf8103b5ff`
- Maltrail Trails release: `content-20261125-2233`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
