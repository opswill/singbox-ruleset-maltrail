# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 125,460 | 93,938 | 25.13% |
| 2 | 36,348 | 26,686 | 26.58% |
| 3 | 20,037 | 14,282 | 28.72% |
| 4 | 11,495 | 8,639 | 24.85% |
| 5 | 5,731 | 4,756 | 17.01% |
| 6 | 2,117 | 1,873 | 11.53% |
| 7 | 497 | 467 | 6.04% |
| 8 | 91 | 90 | 1.10% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,064,128
- Unique domains after exact de-duplication: 1,064,128
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 145,784
- Published `domain_suffix` entries: 918,344

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `11fdd991d1c798836baabf3719e2932d061282dd`
- Maltrail Trails release: `content-20261022-2221`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
