import os
import re
import subprocess
import argparse

# Define regex patterns to match log entries for the bots
bot_patterns = [
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?SemrushBot',      # SemrushBot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?SBIntuitionsBot', # SBIntuitionsBot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?Applebot',        # Applebot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?PetalBot',        # PetalBot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?bingbot',         # Bingbot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?ChatGPT-User',    # ChatGPT-User (OpenAI)
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?SiteAuditBot',    # SiteAuditBot (Semrush)
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?Barkrowler',      # barkrowler 
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?MJ12bot',         # MJ12bot
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?AhrefsBot',       # AhrefsBot 
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?ClaudeBot',       # ClaudeBot 
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?DotBot',          # opensiteexplorer
    r'(\d+\.\d+\.\d+\.\d+) .*?"GET .*?" .*?"Mozilla.*?Bytespider'       # Bytespider    
]

log_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in bot_patterns]

# Store unique IPs to avoid duplicate blocking
blocked_ips = set()

def parse_log_file(log_file):
    """Search a specific Apache log file for bot entries and extract IPs."""
    if not os.path.isfile(log_file):
        print(f"[ERROR] The specified log file does not exist: {log_file}")
        return

    try:
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                for bot_pattern in log_patterns:
                    match = bot_pattern.search(line)
                    if match:
                        ip_address = match.group(1)
                        if ip_address not in blocked_ips:
                            print(f"[!] Found bot ({line.strip()}) from {ip_address}. Blocking...")
                            blocked_ips.add(ip_address)
                            block_ip(ip_address)
    except Exception as e:
        print(f"[ERROR] Could not read {log_file}: {e}")

def block_ip(ip):
    """Block the given IP using UFW."""
    try:
        command = ["sudo", "ufw", "insert", "1", "deny", "from", ip]
        subprocess.run(command, check=True)
        print(f"[+] Successfully blocked {ip}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to block {ip}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a specified Apache log file for specific bots and block their IPs using UFW.")
    parser.add_argument("log_file", help="Path to the Apache log file to scan")

    args = parser.parse_args()
    parse_log_file(args.log_file)
