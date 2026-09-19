# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 123,071 | 93,792 | 23.79% |
| 2 | 33,279 | 25,154 | 24.41% |
| 3 | 17,745 | 12,833 | 27.68% |
| 4 | 9,427 | 6,999 | 25.76% |
| 5 | 4,517 | 3,595 | 20.41% |
| 6 | 1,818 | 1,491 | 17.99% |
| 7 | 603 | 512 | 15.09% |
| 8 | 152 | 138 | 9.21% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 990,274
- Unique domains after exact de-duplication: 990,274
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,950
- Published `domain_suffix` entries: 850,324

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `f5fa01ffaafdf319bd50e94aa9270f63c63c4cbf`
- Maltrail Trails release: `content-20260918-2142`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
