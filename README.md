# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 117,445 | 85,689 | 27.04% |
| 2 | 34,846 | 24,941 | 28.43% |
| 3 | 20,233 | 14,164 | 30.00% |
| 4 | 11,452 | 8,565 | 25.21% |
| 5 | 5,407 | 4,554 | 15.78% |
| 6 | 1,992 | 1,802 | 9.54% |
| 7 | 524 | 483 | 7.82% |
| 8 | 124 | 122 | 1.61% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,062,586
- Unique domains after exact de-duplication: 1,062,586
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 145,604
- Published `domain_suffix` entries: 916,982

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `84387a286db0ffd721f56e738482affbd2ca3bc1`
- Maltrail Trails release: `content-20261019-2254`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
