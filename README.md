# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 141,829 | 99,971 | 29.51% |
| 2 | 35,612 | 25,096 | 29.53% |
| 3 | 18,331 | 12,458 | 32.04% |
| 4 | 10,054 | 7,189 | 28.50% |
| 5 | 4,867 | 4,060 | 16.58% |
| 6 | 1,886 | 1,742 | 7.64% |
| 7 | 492 | 464 | 5.69% |
| 8 | 80 | 75 | 6.25% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,086,256
- Unique domains after exact de-duplication: 1,086,256
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,776
- Published `domain_suffix` entries: 936,480

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `86c6e59d96a39ef16fac51478cbab924028ada17`
- Maltrail Trails release: `content-20261031-2229`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
