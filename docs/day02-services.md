# Day 02 – System Management (Services, Packages, Environment Variables)

---

## 1️⃣ Linux Services

### What is a Service?
A service is a background program that runs continuously and is managed by systemd.

### What is systemd?
systemd is the service manager in modern Linux systems.  
It starts, stops, monitors, and manages services.

### Important Concepts
- PID 1 = systemd
- start → affects current state
- stop → affects current state
- enable → affects boot behavior
- disable → affects boot behavior
- Running state and boot configuration are independent

---

## 2️⃣ Package Management (APT)

### What is APT?
APT (Advanced Package Tool) installs, updates, and removes software packages from repositories.

### Package Lifecycle
Repository → Download → Install → Register Service → Run

### Commands Practiced

### Key Differences
- remove → removes program, keeps config
- purge → removes program + config
- update → refresh package list
- upgrade → install newer versions

---

## 3️⃣ Filesystem Understanding

- /etc → configuration files
- /usr → program binaries
- /var → variable runtime data
- /var/log → logs

Logs are preserved after removal for debugging and investigation.

---

## 4️⃣ Environment Variables

### What Are They?
Environment variables are key-value pairs used to configure system behavior and applications.

### Important Variable
PATH → tells Linux where to find executable programs.

### Create Temporary Variable
export MY_NAME=“DevOpsLearner”
echo $MY_NAME

### Permanent Variable
Add to:~/.bashrc

### Why They Matter
- Store configuration
- Avoid hardcoding secrets
- Used in production deployments
- Control application behavior

---

## 🔎 Key Takeaways

- Services run in the background and are managed by systemd.
- APT installs and maintains software.
- remove vs purge matters in system cleanup.
- Logs are stored in /var/log.
- Environment variables control system and application behavior.
