# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 129,451 | 99,773 | 22.93% |
| 2 | 33,970 | 25,447 | 25.09% |
| 3 | 17,967 | 13,690 | 23.80% |
| 4 | 9,044 | 7,364 | 18.58% |
| 5 | 4,238 | 3,537 | 16.54% |
| 6 | 1,642 | 1,343 | 18.21% |
| 7 | 557 | 460 | 17.41% |
| 8 | 144 | 128 | 11.11% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 982,469
- Unique domains after exact de-duplication: 982,469
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,339
- Published `domain_suffix` entries: 843,130

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `737dc49f40580598d59143e4433e25d25a2d1891`
- Maltrail Trails release: `content-20260914-2231`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
