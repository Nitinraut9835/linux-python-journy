from datetime import datetime

print("Container is running...")
current_time = datetime.now()
print("Current Time:", current_time)

# Write something into a file
with open("output.txt", "w") as f:
    f.write("Docker is working!\n")
    f.write("Time: " + str(current_time) + "\n")

print("Data written to output.txt")
