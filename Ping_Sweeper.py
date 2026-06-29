# ======================
# === Ping Sweeper =====
# ======================

import subprocess
import sys

print("\n=== Ping Sweeper ===\n")

network = input("Enter network (e.g. 192.168.1): ")

print("\nSweeping network...\n")

# _________________________________________________________________________________________________

devices_found = []
total = 254

for i in range(1, 255):

    ip = f"{network}.{i}"

    progress = int((i / total) * 100)
    bar_length = 30
    filled = int(bar_length * i // total)
    bar = "█" * filled + "-" * (bar_length - filled)

    sys.stdout.write(f"\rSweeping: |{bar}| {progress}% ({i}/{total})")
    sys.stdout.flush()

    try:
        result = subprocess.run(["ping", "-n", "1", "-w", "100", ip],
                                capture_output=True,
                                text=True
                                )

        if "ttl=" in result.stdout.lower():
            devices_found.append(ip)
        
    except:
        pass

print("\nSweep Complete.\n")

# _________________________________________________________________________________________________

if devices_found:

    print("Online Devices")
    print("--------------")

    for number, ip in enumerate(devices_found, start=1):
        print(f"{number}. {ip}")

    print(f"\nTotal Devices Found: {len(devices_found)}")

else:
    print("No online devices were found.")
    
# _________________________________________________________________________________________________

