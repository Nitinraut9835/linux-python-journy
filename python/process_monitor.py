import subprocess
import time
import os

while True:
    os.system("clear")

    # Run ps command
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    output = result.stdout
    lines = output.split("\n")

    processes = []

    # Parse process lines
    for line in lines[1:]:
        if line:
            parts = line.split()

            # Defensive check to avoid IndexError
            if len(parts) > 10:
                pid = parts[1]
                cpu = float(parts[2])
                mem = float(parts[3])
                command = " ".join(parts[10:])

                processes.append((pid, cpu, mem, command))

    # Sort by memory usage (change index to 1 for CPU sorting)
    processes.sort(key=lambda x: x[2], reverse=True)

    print("=== Top 5 Memory Consuming Processes ===\n")

    for process in processes[:5]:
        print(f"PID: {process[0]} | CPU: {process[1]}% | MEM: {process[2]}%")
        print(f"Command: {process[3]}")
        print("-" * 50)

    time.sleep(5)
