# Automan - Automated Pentesting Tool

## Overview
Automan is an automated penetration testing tool for reconnaissance, exploitation, privilege escalation, and Metasploit automation.

## Features
- **Reconnaissance**: Nmap scans, subdomain enumeration.
- **Exploitation**: Automated SQL Injection, exploit searches.
- **Privilege Escalation**: Linux & Windows privilege escalation scripts.
- **Reverse Shell**: Payload generation & auto Netcat listener.
- **Metasploit Automation**: Auto-handler setup.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Automan.git
   cd Automan
   ```
2. Install dependencies:
   ```
   sudo apt update
   sudo apt install -y nmap sqlmap metasploit-framework subfinder
   pip install -r requirements.txt
   ```

## Usage
Run the tool and select an option:
```
python3 automan.py --recon
python3 automan.py --exploit
python3 automan.py --priv-esc
python3 automan.py --shell
python3 automan.py --metasploit
```

## Disclaimer
This tool is for educational and ethical hacking purposes only. Use it responsibly.
