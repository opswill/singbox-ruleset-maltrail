# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 123,862 | 96,113 | 22.40% |
| 2 | 32,986 | 25,226 | 23.53% |
| 3 | 16,927 | 13,275 | 21.57% |
| 4 | 8,679 | 7,241 | 16.57% |
| 5 | 4,059 | 3,507 | 13.60% |
| 6 | 1,541 | 1,300 | 15.64% |
| 7 | 510 | 405 | 20.59% |
| 8 | 155 | 132 | 14.84% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 975,131
- Unique domains after exact de-duplication: 975,131
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,165
- Published `domain_suffix` entries: 835,966

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `8af8e74d17a351d37d2057e3ff7202c066d24a72`
- Maltrail Trails release: `content-20260912-0548`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
