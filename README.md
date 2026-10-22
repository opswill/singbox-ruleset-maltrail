# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 120,591 | 90,627 | 24.85% |
| 2 | 35,394 | 25,638 | 27.56% |
| 3 | 19,858 | 14,620 | 26.38% |
| 4 | 10,892 | 8,648 | 20.60% |
| 5 | 5,316 | 4,621 | 13.07% |
| 6 | 1,841 | 1,682 | 8.64% |
| 7 | 394 | 368 | 6.60% |
| 8 | 60 | 59 | 1.67% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,064,033
- Unique domains after exact de-duplication: 1,064,033
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 145,771
- Published `domain_suffix` entries: 918,262

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `724f4cb664f2ae38a7a8ed8618a5e0aac6dbb7e9`
- Maltrail Trails release: `content-20261021-2222`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
