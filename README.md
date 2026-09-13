# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 127,046 | 98,639 | 22.36% |
| 2 | 33,342 | 24,901 | 25.32% |
| 3 | 18,632 | 13,477 | 27.67% |
| 4 | 9,969 | 7,839 | 21.37% |
| 5 | 4,677 | 3,874 | 17.17% |
| 6 | 1,842 | 1,536 | 16.61% |
| 7 | 642 | 541 | 15.73% |
| 8 | 181 | 166 | 8.29% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 976,664
- Unique domains after exact de-duplication: 976,664
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,308
- Published `domain_suffix` entries: 837,356

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `aca1d527ebc735c084ece9fb1e099bb9eca883e1`
- Maltrail Trails release: `content-20260913-0611`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
