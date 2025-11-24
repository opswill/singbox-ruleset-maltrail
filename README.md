# Sing-box Maltrail Rule Set

[![Update Maltrail Ruleset](https://github.com/opswill/singbox-ruleset-maltrail/actions/workflows/update-maltrail.yml/badge.svg)](https://github.com/opswill/singbox-ruleset-maltrail/actions/workflows/update-maltrail.yml)

本项目通过 GitHub Actions 自动每日抓取 [Maltrail](https://github.com/stamparm/maltrail) 提供的恶意软件 IP 和域名列表，并将其编译为 **Sing-box** 专用的二进制规则集 (`.srs`)。

使用此规则集可以在网关或设备拦截已知的恶意流量、僵尸网络和恶意软件域名。

## 📋 规则集列表

本项目维护两个独立分支来存放不同格式的规则文件：

- **`rule-set` 分支**：存放编译好的 `.srs` 文件，供 Sing-box 直接使用。
- **`text` 分支**：存放原始 `.txt` 文件，供其他工具（如 Surge, Clash, 防火墙脚本）或数据分析使用。

### 1. Sing-box 二进制规则 (SRS)

*位于 `rule-set` 分支*

| 类型 | 文件名 | 描述 | 下载链接 (Raw) |
| :--- | :--- | :--- | :--- |
| **恶意 IP** | `maltrail_ip.srs` | Maltrail 识别的高风险恶意 IP (CIDR) | [点击复制链接](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_ip.srs) |
| **恶意域名** | `maltrail_domain.srs` | Maltrail 识别的恶意软件传播域名 | [点击复制链接](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/rule-set/maltrail_domain.srs) |

### 2. 原始文本规则 (Text)
*位于 `text` 分支*

| 类型 | 文件名 | 描述 | 下载链接 (Raw) |
| :--- | :--- | :--- | :--- |
| **恶意 IP** | `maltrail_ip.txt` | 纯文本格式，每行一个 IP 或 CIDR | [点击复制链接](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/text/maltrail_ip.txt) |
| **恶意域名** | `maltrail_domain.txt` | 纯文本格式，每行一个域名 | [点击复制链接](https://raw.githubusercontent.com/opswill/singbox-ruleset-maltrail/text/maltrail_domain.txt) |

---

## ⚙️ 如何在 Sing-box 中使用

在您的 Sing-box `config.json` 配置文件中，需要在`dns` 及 `route` 部分添加 `rule_set` 定义，并在 `rules` 中引用它们进行拦截（通常建议设置为 `reject`）。

### 配置示例

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
                "type": "logical",
                "mode": "or",
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
        ]
    }
}
```

## 📚 数据来源

本项目的原始数据来源于 Maltrail 项目维护的公开列表：

- IP List: [stamparm/ipsum (Level 1 - High confidence)](https://raw.githubusercontent.com/stamparm/ipsum/refs/heads/master/levels/1.txt)

- Domain List: [stamparm/aux](https://raw.githubusercontent.com/stamparm/aux/master/maltrail-malware-domains.txt)

感谢原项目及作者的贡献。

## ⚠️ 免责声明

本规则集仅基于开源情报自动生成，不保证 100% 的准确性或误报率。
请根据您的实际网络环境谨慎使用。
