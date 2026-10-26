# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 130,472 | 95,576 | 26.75% |
| 2 | 36,598 | 25,767 | 29.59% |
| 3 | 19,922 | 13,602 | 31.72% |
| 4 | 11,681 | 7,893 | 32.43% |
| 5 | 5,986 | 4,687 | 21.70% |
| 6 | 2,147 | 1,922 | 10.48% |
| 7 | 489 | 465 | 4.91% |
| 8 | 85 | 82 | 3.53% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,076,842
- Unique domains after exact de-duplication: 1,076,842
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 147,394
- Published `domain_suffix` entries: 929,448

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `14c7e25bf8345e87b221be04d6a127e006ef2e36`
- Maltrail Trails release: `content-20261025-2148`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
