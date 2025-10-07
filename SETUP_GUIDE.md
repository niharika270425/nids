//Step-by-step setup instructions.

mkdir docs
nano docs/SETUP_GUIDE.md
#add this content

//NIDS Setup Guide

## 1. Install Suricata
## 2. Install Oinkmaster (Rule Manager)

//bash sudo apt install oinkmaster -y
Edit `/etc/oinkmaster.conf`:

url = https://rules.emergingthreats.net/open/suricata-6.0.0/emerging.rules.tar.gz

Update rules:
bash sudo oinkmaster -C /etc/oinkmaster.conf -o /etc/suricata/rules/
## 3. Copy Configuration
Replace default config with our version:

bash sudo cp config/suricata.yaml /etc/suricata/suricata.yaml
## 4. Start Suricata

bash sudo suricata -c /etc/suricata/suricata.yaml -i eth0
## 5. Run Auto-Block Script
Make executable:

bash chmod +x scripts/block_malicious_ips.py
Run manually or via cron:

## 6. View Logs
bash tail -f /var/log/suricata/fast.log

## 7. (Optional) Set Up EveBox Dashboard
bash wget https://github.com/jasonish/evebox/releases/latest/download/evebox_0.12.1_amd64.deb sudo dpkg -i evebox_0.12.1_amd64.deb sudo evebox server -v --datastore sqlite
Access: `http://your-server:5636`

