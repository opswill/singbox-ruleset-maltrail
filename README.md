# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 140,106 | 99,202 | 29.20% |
| 2 | 39,922 | 29,765 | 25.44% |
| 3 | 18,355 | 13,967 | 23.91% |
| 4 | 8,452 | 6,933 | 17.97% |
| 5 | 2,874 | 2,525 | 12.14% |
| 6 | 715 | 648 | 9.37% |
| 7 | 158 | 150 | 5.06% |
| 8 | 33 | 32 | 3.03% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,145,415
- Unique domains after exact de-duplication: 1,145,415
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 170,974
- Published `domain_suffix` entries: 974,441

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `267631bb580e40c5a60035f79e0663403a6da218`
- Maltrail Trails release: `content-20261118-2126`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
