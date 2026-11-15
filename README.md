# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 136,069 | 92,607 | 31.94% |
| 2 | 39,353 | 27,753 | 29.48% |
| 3 | 18,171 | 13,013 | 28.39% |
| 4 | 9,085 | 7,026 | 22.66% |
| 5 | 3,613 | 3,164 | 12.43% |
| 6 | 953 | 888 | 6.82% |
| 7 | 196 | 189 | 3.57% |
| 8 | 38 | 38 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,119,418
- Unique domains after exact de-duplication: 1,119,418
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 157,627
- Published `domain_suffix` entries: 961,791

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `d04890974d322d57e0bcd20960660f448d71432f`
- Maltrail Trails release: `content-20261114-2259`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
