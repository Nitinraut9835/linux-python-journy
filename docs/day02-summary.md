# Day 02 – System Management & Process Monitoring

## 🔹 Linux Concepts Learned

### Services & systemd
- systemd is PID 1
- start/stop affect current state
- enable/disable affect boot behavior
- Running state and boot state are independent

### Package Management (APT)
- install, remove, purge
- remove keeps config
- purge removes config
- update refreshes package list
- upgrade installs new versions

### Filesystem Understanding
- /etc → configuration
- /usr → binaries
- /var → runtime data
- /var/log → logs

### Environment Variables
- PATH controls command lookup
- export makes variable available to child processes
- Order in PATH matters

---

## 🔹 Python Process Monitor Project

### Goal
Build a script that:
- Runs `ps aux`
- Extracts PID, CPU, Memory, Command
- Sorts by memory usage
- Displays top 5 processes
- Refreshes every 5 seconds

### Technical Concepts Used
- subprocess.run()
- capture_output=True
- text=True
- string splitting
- list slicing
- defensive checks (len(parts))
- float conversion
- sorting with lambda
- infinite loop
- time.sleep()
- os.system("clear")

---

## 🔹 Problems Faced
- IndentationError (Python block structure)
- Accidental tuple creation using comma
- IndexError risk when parsing lines
- Understanding difference between string vs float sorting

---

## 🔹 Key Learning
- Everything running in Linux is a process
- Services are managed by systemd
- Programs are found using PATH
- Monitoring requires structured parsing
- Small mistakes in parsing can break logic

---
