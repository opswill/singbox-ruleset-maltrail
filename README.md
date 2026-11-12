# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 133,241 | 93,301 | 29.98% |
| 2 | 35,694 | 25,534 | 28.46% |
| 3 | 17,596 | 12,303 | 30.08% |
| 4 | 8,764 | 6,473 | 26.14% |
| 5 | 3,708 | 3,218 | 13.21% |
| 6 | 1,082 | 1,014 | 6.28% |
| 7 | 251 | 237 | 5.58% |
| 8 | 63 | 59 | 6.35% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,103,347
- Unique domains after exact de-duplication: 1,103,347
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 154,456
- Published `domain_suffix` entries: 948,891

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `2b38793decac3cbb217b392d6968a8074a220539`
- Maltrail Trails release: `content-20261111-2012`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
