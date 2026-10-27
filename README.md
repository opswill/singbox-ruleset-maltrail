# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 137,843 | 100,431 | 27.14% |
| 2 | 37,019 | 26,563 | 28.24% |
| 3 | 19,862 | 13,883 | 30.10% |
| 4 | 11,477 | 8,254 | 28.08% |
| 5 | 5,873 | 4,698 | 20.01% |
| 6 | 2,062 | 1,853 | 10.14% |
| 7 | 522 | 492 | 5.75% |
| 8 | 96 | 93 | 3.12% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,079,166
- Unique domains after exact de-duplication: 1,079,166
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,152
- Published `domain_suffix` entries: 930,014

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `a532a0b27bb8553b1bdc9bf8ac4707f4d9cc98ae`
- Maltrail Trails release: `content-20261026-2308`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
