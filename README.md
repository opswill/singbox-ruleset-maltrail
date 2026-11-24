# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 130,701 | 96,480 | 26.18% |
| 2 | 37,369 | 27,293 | 26.96% |
| 3 | 16,564 | 12,091 | 27.00% |
| 4 | 7,535 | 5,765 | 23.49% |
| 5 | 2,398 | 1,978 | 17.51% |
| 6 | 673 | 602 | 10.55% |
| 7 | 130 | 125 | 3.85% |
| 8 | 17 | 17 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,149,357
- Unique domains after exact de-duplication: 1,149,357
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 171,540
- Published `domain_suffix` entries: 977,817

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `3bfb0fa1a17afe8608b7b38ca9d7202d270e413a`
- Maltrail Trails release: `content-20261123-0907`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
