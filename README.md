# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 137,086 | 99,505 | 27.41% |
| 2 | 39,915 | 29,514 | 26.06% |
| 3 | 18,821 | 13,058 | 30.62% |
| 4 | 10,505 | 7,869 | 25.09% |
| 5 | 4,197 | 3,430 | 18.27% |
| 6 | 1,208 | 1,049 | 13.16% |
| 7 | 242 | 220 | 9.09% |
| 8 | 63 | 60 | 4.76% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,082,722
- Unique domains after exact de-duplication: 1,082,722
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 149,616
- Published `domain_suffix` entries: 933,106

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `4ef94e56f9e9edf44ca64a8be3497a89f2a4c365`
- Maltrail Trails release: `content-20261027-2257`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
