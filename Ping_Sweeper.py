# ======================
# === Ping Sweeper =====
# ======================

import subprocess

print("\n=== Ping Sweeper ===\n")

network = input("Enter network (e.g. 192.168.1): ")

print("\nSweeping network...\n")

devices_found = []

for i in range(1, 255):

    ip = f"{network}.{i}"
    print(f"Checking {ip}...", end="\r")

    result = subprocess.run(["ping", "-n", "1", "-w", "100", ip],
                            capture_output=True,
                            text=True
                            )

    if "ttl=" in result.stdout.lower():
        devices_found.append(ip)

print("\nSweep Complete.\n")

