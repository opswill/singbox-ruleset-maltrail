# Sing-box Maltrail Rule Set

[![Update Maltrail Ruleset](https://github.com/opswill/singbox-ruleset-maltrail/actions/workflows/update-maltrail.yml/badge.svg)](https://github.com/opswill/singbox-ruleset-maltrail/actions/workflows/update-maltrail.yml)

[English](README_en-US.md) | [中文](README.md)

This project utilizes GitHub Actions to automatically fetch the malicious IP and domain lists from [Maltrail](https://github.com/stamparm/maltrail) daily, compiling them into **Sing-box**'s proprietary binary Rule Sets (`.srs`). These rules can be used on your gateway or device to block known malicious traffic, botnets, and malware domains.

## 📋 Rule Set Lists

This repository maintains two separate branches to store the rule files in different formats:

- **`rule-set` branch**: Stores the compiled `.srs` files, ready for direct use by Sing-box.
- **`text` branch**: Stores the raw `.txt` files, suitable for use with other tools (e.g., Surge, Clash, firewall scripts) or for data analysis.

### 1. Sing-box Binary Rules (SRS)

*Located on the `rule-set` branch*

| Type | Filename | Description | Download Link (Raw) |
| :--- | :--- | :--- | :--- |
| **Malicious IP** | `maltrail_ip.srs` | High-risk malicious IP addresses (CIDR) identified by Maltrail. | [Copy URL](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_ip.srs) |
| **Malicious Domain** | `maltrail_domain.srs` | Malware propagation domains identified by Maltrail. | [Copy URL](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_domain.srs) |

### 2. Raw Text Rules (Text)
*Located on the `text` branch*

| Type | Filename | Description | Download Link (Raw) |
| :--- | :--- | :--- | :--- |
| **Malicious IP** | `maltrail_ip.txt` | Plain text format, one IP or CIDR per line. | [Copy URL](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/text/maltrail_ip.txt) |
| **Malicious Domain** | `maltrail_domain.txt` | Plain text format, one domain per line. | [Copy URL](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/text/maltrail_domain.txt) |

---

## ⚙️ Usage in Sing-box

In your Sing-box `config.json`, you need to define the remote `rule_set` blocks in the `route` section and reference them for blocking (`"action": "reject"`) in both the `dns` and `route` rules.

### Configuration Example

```json
{
    "dns": {
        "servers": [
            {
                // dns servers
            }
        ],
        "rules": [
            {
                "rule_set": [
                    "maltrail-domain"
                ],
                "action": "reject"
            }
        ]
    },
    "route": {
        "rule_set": [
            {
                "tag": "maltrail-domain",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_domain.srs",
                "download_detour": "proxy-github"
            },
            {
                "tag": "maltrail-ip",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_ip.srs",
                "download_detour": "proxy-github"
            }
        ],
        "rules": [
            {
                "action": "sniff"
            },
            {
                "type": "logical",
                "mode": "or",
                "rules": [
                    {
                        "protocol": "dns"
                    },
                    {
                        "port": 53
                    }
                ],
                "action": "hijack-dns"
            },
            {
                "rule_set": [
                    "maltrail-domain"
                ],
                "action": "reject"
            },
            {
                "action": "resolve"
            },
            {
                "rule_set": [
                    "maltrail-ip"
                ],
                "action": "reject"
            }
        ]
    }
}
```

## 📚 Data Sources

The raw data for this project is sourced from the public lists maintained by the Maltrail project:

- IP List: [stamparm/ipsum (Level 1 - High confidence)](https://raw.githubusercontent.com/stamparm/ipsum/refs/heads/master/levels/1.txt)

- Domain List: [stamparm/aux](https://raw.githubusercontent.com/stamparm/aux/master/maltrail-malware-domains.txt)

Thanks to the original project and contributors for their efforts.

## 🔄 Update Mechanism

Update Frequency: GitHub Actions runs automatically every day at 04:00 UTC.

## ⚠️ Disclaimer

This rule set is automatically generated based solely on open-source intelligence. We do not guarantee 100% accuracy or freedom from false positives. Please use at your own discretion based on your network environment.
