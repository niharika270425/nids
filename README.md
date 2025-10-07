
# Network Intrusion Detection System (NIDS) with Suricata

A fully documented NIDS setup using **Suricata** to monitor, detect, and respond to network threats.

##  Features
- Real-time traffic monitoring
- Rule-based threat detection (Emerging Threats)
- Automatic IP blocking on alerts
- Alert logging (`fast.log`, `eve.json`)
- Optional visualization (EveBox/ELK)

nids-suricata/ ├── config/ # Suricata configuration ├── scripts/ # Automation scripts ├── docs/ # Documentation ├── .github/workflows/ # CI/CD and monitoring └── .gitignore # Exclude logs/secrets



##  Getting Started
See [docs/SETUP_GUIDE.md](SETUP_GUIDE.md) for full setup instructions.

## Visualization
Use [EveBox](https://github.com/jasonish/evebox) or ELK Stack to view alerts in a dashboard.

