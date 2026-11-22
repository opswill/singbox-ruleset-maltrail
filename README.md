# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 139,496 | 97,922 | 29.80% |
| 2 | 40,586 | 29,648 | 26.95% |
| 3 | 20,087 | 14,627 | 27.18% |
| 4 | 9,398 | 7,084 | 24.62% |
| 5 | 3,261 | 2,743 | 15.88% |
| 6 | 904 | 810 | 10.40% |
| 7 | 229 | 213 | 6.99% |
| 8 | 48 | 46 | 4.17% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,148,821
- Unique domains after exact de-duplication: 1,148,821
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 171,430
- Published `domain_suffix` entries: 977,391

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `2165208853761211859615c17a487dca3522128e`
- Maltrail Trails release: `content-20261121-2006`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
