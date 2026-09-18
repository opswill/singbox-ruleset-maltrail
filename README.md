# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 124,048 | 95,548 | 22.97% |
| 2 | 35,334 | 26,917 | 23.82% |
| 3 | 18,924 | 14,544 | 23.15% |
| 4 | 9,849 | 7,757 | 21.24% |
| 5 | 4,835 | 3,927 | 18.78% |
| 6 | 2,007 | 1,625 | 19.03% |
| 7 | 707 | 601 | 14.99% |
| 8 | 204 | 188 | 7.84% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 989,433
- Unique domains after exact de-duplication: 989,433
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 139,543
- Published `domain_suffix` entries: 849,890

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `7cd8235be6154f9ed9fdc7282f5adda79725a130`
- Maltrail Trails release: `content-20260917-2232`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
