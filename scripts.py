mkdir scripts
nano scripts/block_malicious_ips.py


#!/usr/bin/env python3
"""
Auto-block IPs from Suricata fast.log
"""
import re
import subprocess
from datetime import datetime

LOG_FILE = "/var/log/suricata/fast.log"
BLOCKED_LOG = "/var/log/suricata/blocked_ips.log"

def block_ip(ip):
    try:
        subprocess.run(["sudo", "iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"IP {ip} already blocked.")
    except subprocess.CalledProcessError:
        # IP not blocked yet, so block it
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        with open(BLOCKED_LOG, "a") as f:
            f.write(f"{datetime.now()}: Blocked {ip}\n")
        print(f"Blocked {ip}")

# Read log and scan for alerts
with open(LOG_FILE, "r") as f:
    for line in f:
        if "ATTACK" in line or "MALWARE" in line or "SCAN" in line:
            ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line)
            if ip_match:
                block_ip(ip_match.group())
