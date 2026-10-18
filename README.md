# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 122,301 | 87,131 | 28.76% |
| 2 | 34,296 | 23,951 | 30.16% |
| 3 | 19,091 | 12,852 | 32.68% |
| 4 | 10,781 | 7,771 | 27.92% |
| 5 | 5,102 | 4,280 | 16.11% |
| 6 | 1,753 | 1,603 | 8.56% |
| 7 | 403 | 384 | 4.71% |
| 8 | 65 | 64 | 1.54% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,058,175
- Unique domains after exact de-duplication: 1,058,175
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 144,338
- Published `domain_suffix` entries: 913,837

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `d86edbc1c8c772b991c8d4cbf714364795799763`
- Maltrail Trails release: `content-20261017-2128`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
