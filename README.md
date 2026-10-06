# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 112,522 | 84,704 | 24.72% |
| 2 | 32,741 | 24,462 | 25.29% |
| 3 | 16,660 | 12,632 | 24.18% |
| 4 | 8,710 | 7,297 | 16.22% |
| 5 | 4,122 | 3,660 | 11.21% |
| 6 | 1,710 | 1,573 | 8.01% |
| 7 | 545 | 510 | 6.42% |
| 8 | 74 | 71 | 4.05% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,014,063
- Unique domains after exact de-duplication: 1,014,063
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,355
- Published `domain_suffix` entries: 870,708

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `0f1a6144c1fd16e071f8d3d1b7023588977bb759`
- Maltrail Trails release: `content-20261006-0049`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
