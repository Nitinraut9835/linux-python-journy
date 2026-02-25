# Import tools we need
import subprocess
import datetime

# 1. Get current date and time
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# 2. Get disk usage information
disk_result = subprocess.run(["df", "-h"], capture_output=True, text=True)
disk_output = disk_result.stdout

# 3. Get memory usage information
memory_result = subprocess.run(["free", "-m"], capture_output=True, text=True)
memory_output = memory_result.stdout

# 4. Create the report text
report = "SYSTEM REPORT\n"
report += "Generated at: " + current_time + "\n\n"

report += "DISK USAGE:\n"
report += disk_output + "\n"

report += "MEMORY USAGE:\n"
report += memory_output + "\n"

# 5. Save the report to a file
file = open("report.txt", "w")
file.write(report)
file.close()

print("Report generated successfully!")
