# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 111,822 | 90,958 | 18.66% |
| 2 | 33,516 | 25,285 | 24.56% |
| 3 | 17,875 | 13,385 | 25.12% |
| 4 | 9,114 | 7,014 | 23.04% |
| 5 | 3,875 | 2,920 | 24.65% |
| 6 | 1,439 | 1,033 | 28.21% |
| 7 | 532 | 383 | 28.01% |
| 8 | 109 | 92 | 15.60% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 996,050
- Unique domains after exact de-duplication: 996,050
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 140,392
- Published `domain_suffix` entries: 855,658

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `57bdc3f924329e95602898adcd0dbafc1a9861ee`
- Maltrail Trails release: `content-20260922-2209`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
