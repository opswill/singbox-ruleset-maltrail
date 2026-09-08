# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 131,282 | 101,958 | 22.34% |
| 2 | 33,281 | 25,544 | 23.25% |
| 3 | 17,689 | 13,275 | 24.95% |
| 4 | 8,274 | 6,647 | 19.66% |
| 5 | 3,666 | 3,107 | 15.25% |
| 6 | 1,203 | 1,029 | 14.46% |
| 7 | 374 | 319 | 14.71% |
| 8 | 89 | 81 | 8.99% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 971,701
- Unique domains after exact de-duplication: 971,701
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 138,759
- Published `domain_suffix` entries: 832,942

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `6ea2a9e0d9d15486a1dc5a89e8b14edbf5f98fb4`
- Maltrail Trails release: `content-20260907-2202`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
