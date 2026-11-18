# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 138,872 | 98,413 | 29.13% |
| 2 | 39,030 | 28,918 | 25.91% |
| 3 | 18,339 | 13,504 | 26.36% |
| 4 | 9,200 | 7,068 | 23.17% |
| 5 | 3,629 | 3,147 | 13.28% |
| 6 | 1,085 | 1,007 | 7.19% |
| 7 | 290 | 276 | 4.83% |
| 8 | 64 | 62 | 3.12% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,145,172
- Unique domains after exact de-duplication: 1,145,172
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 170,930
- Published `domain_suffix` entries: 974,242

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `ff5e82cb8daafab6806a939653783e3d3149e77f`
- Maltrail Trails release: `content-20261117-2146`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
