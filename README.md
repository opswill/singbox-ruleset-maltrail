# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 112,066 | 82,526 | 26.36% |
| 2 | 32,116 | 23,194 | 27.78% |
| 3 | 16,812 | 12,116 | 27.93% |
| 4 | 8,507 | 6,497 | 23.63% |
| 5 | 3,531 | 2,832 | 19.80% |
| 6 | 1,213 | 976 | 19.54% |
| 7 | 295 | 248 | 15.93% |
| 8 | 46 | 39 | 15.22% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,013,562
- Unique domains after exact de-duplication: 1,013,562
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,219
- Published `domain_suffix` entries: 870,343

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `f2a591df5fcfc0a76ebd2fdd9957c61065ba02a3`
- Maltrail Trails release: `content-20261004-2220`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
