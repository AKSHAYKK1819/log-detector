import re
from collections import defaultdict

log_file = "test.log"

ip_pattern = r"\d+\.\d+\.\d+\.\d+"

attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = re.search(ip_pattern, line)
            if ip:
                attempts[ip.group()] += 1

print("\nSuspicious Login Attempts\n")

for ip, count in attempts.items():
    if count >= 3:
        print(f"Possible brute force attack from {ip} ({count} attempts)")

