# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 127,507 | 97,101 | 23.85% |
| 2 | 35,145 | 26,832 | 23.65% |
| 3 | 18,842 | 14,444 | 23.34% |
| 4 | 9,498 | 7,584 | 20.15% |
| 5 | 4,822 | 3,979 | 17.48% |
| 6 | 1,985 | 1,656 | 16.57% |
| 7 | 649 | 534 | 17.72% |
| 8 | 176 | 149 | 15.34% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 996,144
- Unique domains after exact de-duplication: 996,144
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,402
- Published `domain_suffix` entries: 855,742

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `167c63626fd82fe6aa84dd780a32dbcdb1bb86f2`
- Maltrail Trails release: `content-20260923-2218`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
