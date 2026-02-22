import os

directory = input("Enter directory path: ")
files =  os.listdir(directory)

print("file found: ")
for file in files:
     print(file)

txt_count = 0
py_count = 0
log_count = 0

for file in files:
    if file.endswith(".txt"):
        txt_count += 1
    elif file.endswith(".py"):
        py_count += 1
    elif file.endswith(".log"):
       log_count += 1
print("\nFile counts:")
print(".txt files:", txt_count)
print(".py files:", py_count)
print(".log files:", log_count)
