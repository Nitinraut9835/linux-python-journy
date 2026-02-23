import subprocess

result = subprocess.run(["ps", "aux"], capture_output=True, text=True)

output = result.stdout
lines  = output.split("\n")

processes = []

for line in lines[1:]:
    if line:
      parts = line.split()
      PID = parts[1]
      mem =float(parts[3])
      command = " ".join(parts[10:])
      processes.sort(key=lambda x: x[1], reverse=True)
      processes.append((PID, mem, command))

print("\nTop 5 Memory Consuming Processes:\n")

for process in processes[:5]:
    pid = process[0]
    mem = process[1]
    command = process[2]

    print(f"PID: {pid} | Memory: {mem}% | Command: {command}")
#      print(processes[:5])
#      print("PID:", PID, "| Memory:", mem, "| Command:", command)
#      print(type(mem))
#first_process = lines[1]
#parts = first_process.split()

#PID = parts[1]
#mem = parts[3]
#command = parts[10]

#print("PID:",PID)
#print("Memory:", mem)
#print("Command:", command)
