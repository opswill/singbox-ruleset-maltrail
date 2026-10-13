# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 121,578 | 87,636 | 27.92% |
| 2 | 34,472 | 24,084 | 30.13% |
| 3 | 19,682 | 13,128 | 33.30% |
| 4 | 10,979 | 7,928 | 27.79% |
| 5 | 5,079 | 4,164 | 18.02% |
| 6 | 2,038 | 1,743 | 14.47% |
| 7 | 633 | 559 | 11.69% |
| 8 | 134 | 128 | 4.48% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,045,485
- Unique domains after exact de-duplication: 1,045,485
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 143,889
- Published `domain_suffix` entries: 901,596

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `444b48029c5f73a8d082d292bca1c5893638b08b`
- Maltrail Trails release: `content-20261012-2144`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.txt` ... `ipsum-level-8.txt`
- `maltrail-malware-domains.txt`
- `maltrail-malware-domains-full.txt` (exact de-duplicated IOC inventory)
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.txt` -> `ipsum-level-1.txt`
- `maltrail_domain.txt` -> exact de-duplicated `maltrail-malware-domains-full.txt` (legacy text compatibility)
