# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 123,060 | 95,077 | 22.74% |
| 2 | 31,579 | 23,778 | 24.70% |
| 3 | 16,482 | 12,676 | 23.09% |
| 4 | 8,546 | 7,119 | 16.70% |
| 5 | 4,011 | 3,444 | 14.14% |
| 6 | 1,525 | 1,300 | 14.75% |
| 7 | 497 | 406 | 18.31% |
| 8 | 161 | 141 | 12.42% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 975,007
- Unique domains after exact de-duplication: 975,007
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,139
- Published `domain_suffix` entries: 835,868

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `c6eb2be1e1d15b6165cfac07726c35c2ac81129e`
- Maltrail Trails release: `content-20260910-2138`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
