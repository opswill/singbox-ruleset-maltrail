# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 137,802 | 93,517 | 32.14% |
| 2 | 39,315 | 27,888 | 29.07% |
| 3 | 18,640 | 13,017 | 30.17% |
| 4 | 9,520 | 7,035 | 26.10% |
| 5 | 3,855 | 3,406 | 11.65% |
| 6 | 985 | 938 | 4.77% |
| 7 | 202 | 194 | 3.96% |
| 8 | 34 | 34 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,104,056
- Unique domains after exact de-duplication: 1,104,056
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 154,581
- Published `domain_suffix` entries: 949,475

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `160d7cb71a7250d62241a001a6fd45561f95fc26`
- Maltrail Trails release: `content-20261112-2050`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
