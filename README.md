# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 117,151 | 86,793 | 25.91% |
| 2 | 33,051 | 23,904 | 27.68% |
| 3 | 18,009 | 12,763 | 29.13% |
| 4 | 9,391 | 7,098 | 24.42% |
| 5 | 4,372 | 3,633 | 16.90% |
| 6 | 1,428 | 1,261 | 11.69% |
| 7 | 273 | 254 | 6.96% |
| 8 | 46 | 45 | 2.17% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,007,989
- Unique domains after exact de-duplication: 1,007,989
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,004
- Published `domain_suffix` entries: 864,985

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `7ee826cc9783585c8a2c51c798edc09fb071f847`
- Maltrail Trails release: `content-20261001-2313`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
