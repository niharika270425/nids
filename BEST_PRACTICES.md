nano docs/BEST_PRACTICES.md


#  NIDS Best Practices

## Security
- Never hardcode secrets or IPs in config files.
- Run Suricata in a non-root user mode if possible.
- Use `sudo` only when necessary.

##  Updates
- Update rules weekly using Oinkmaster.
- Keep Suricata updated: `sudo apt upgrade suricata`

##  Logging
- Archive old logs (`fast.log`, `eve.json`) regularly.
- Use log rotation: `logrotate`

##  False Positives
- Tune rules to reduce noise.
- Disable irrelevant rules (e.g., test rules in lab only).

##  Monitoring
- Integrate with SIEM (Wazuh, Splunk, ELK).
- Set up email alerts using `swatch` or custom scripts.

##  Testing
- Test detection with tools like `nmap`, `metasploit`, or `suricata-verify`.
- Use PCAP files to simulate attacks.
