# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 130,055 | 101,247 | 22.15% |
| 2 | 36,253 | 27,839 | 23.21% |
| 3 | 19,549 | 15,056 | 22.98% |
| 4 | 9,969 | 8,135 | 18.40% |
| 5 | 4,859 | 4,173 | 14.12% |
| 6 | 1,931 | 1,637 | 15.23% |
| 7 | 652 | 551 | 15.49% |
| 8 | 159 | 140 | 11.95% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 996,507
- Unique domains after exact de-duplication: 996,507
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,453
- Published `domain_suffix` entries: 856,054

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `b72d389909f5089fbb233fe91ef01571b634cc44`
- Maltrail Trails release: `content-20260924-2225`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
