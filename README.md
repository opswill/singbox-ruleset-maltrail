# Generated security rule sets

## IPsum

Levels 1-8 are generated from one pinned `ipsum.txt` snapshot. Duplicate IPs are removed first, then each level is exactly collapsed into CIDRs. The build verifies that the collapsed address set is identical to the source address set, so no unrelated IP can be introduced.

| Level | Unique IPs | Published IP/CIDR entries | Entry reduction |
|---:|---:|---:|---:|
| 1 | 119,838 | 86,904 | 27.48% |
| 2 | 34,476 | 24,779 | 28.13% |
| 3 | 19,786 | 13,272 | 32.92% |
| 4 | 10,827 | 7,750 | 28.42% |
| 5 | 4,946 | 4,092 | 17.27% |
| 6 | 1,730 | 1,559 | 9.88% |
| 7 | 472 | 447 | 5.30% |
| 8 | 75 | 75 | 0.00% |

## Maltrail malware domains

The source is the official `maltrail-malware-domains.txt` derived from Maltrail Trails `malware/` content.

- Raw rows: 1,059,198
- Unique domains after exact de-duplication: 1,059,198
- Exact duplicate rows removed: 0
- Redundant child suffixes removed: 144,444
- Published `domain_suffix` entries: 914,754

Suffix compaction is label-aware: a child such as `a.example.com` is removed only when `example.com` itself exists in the source list. A string such as `badexample.com` is not considered a child of `example.com`.

## Source snapshots

- IPsum commit: `223ca5d8ada329b0ca32412fd818c9220a7eb969`
- Maltrail Trails release: `content-20261018-2131`
- sing-box compiler: `v1.14.0`
- sing-box source rule-set version: `2`

## Files

- `ipsum-level-1.srs` ... `ipsum-level-8.srs`
- `maltrail-malware-domains.srs`
- `manifest.json`

## Compatibility aliases

- `maltrail_ip.srs` -> `ipsum-level-1.srs`
- `maltrail_domain.srs` -> `maltrail-malware-domains.srs`
