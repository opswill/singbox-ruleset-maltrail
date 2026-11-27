# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 145,238 | 101,579 | 30.06% |
| 2 | 38,900 | 27,954 | 28.14% |
| 3 | 17,606 | 12,680 | 27.98% |
| 4 | 8,367 | 6,467 | 22.71% |
| 5 | 2,990 | 2,631 | 12.01% |
| 6 | 900 | 840 | 6.67% |
| 7 | 194 | 193 | 0.52% |
| 8 | 33 | 32 | 3.03% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,155,655
- Unique domains after exact de-duplication: 1,155,655
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 173,172
- Published `domain_suffix` entries: 982,483

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `0d4e2f32cf0cd3ab9006af2af2f3394765743ce6`
- Maltrail Trails release: `content-20261126-2221`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
