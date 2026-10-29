# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 141,943 | 103,386 | 27.16% |
| 2 | 42,979 | 32,512 | 24.35% |
| 3 | 19,879 | 13,910 | 30.03% |
| 4 | 11,613 | 8,398 | 27.68% |
| 5 | 6,086 | 4,897 | 19.54% |
| 6 | 2,389 | 2,149 | 10.05% |
| 7 | 580 | 556 | 4.14% |
| 8 | 101 | 98 | 2.97% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,085,410
- Unique domains after exact de-duplication: 1,085,410
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,627
- Published `domain_suffix` entries: 935,783

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `d507546c1082006371b8d3b33d7f8a8d49c8b775`
- Maltrail Trails release: `content-20261028-2314`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
