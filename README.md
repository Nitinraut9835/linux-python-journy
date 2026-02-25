# Linux & Python System Engineering Journey

This repository documents my structured 3-month journey to strengthen:

- Linux fundamentals
- System administration concepts
- Process management
- Python automation
- Monitoring tools

---

## 📅 Progress

### Day 01
- Linux filesystem practice
- Permissions
- Process basics
- File automation scripts

### Day 02
- Services & systemd
- Package management (APT)
- Environment variables
- Built real-time process monitoring script

### Day 03
- Built Bash backup automation script
- Learned positional arguments ($1)
- Learned directory validation (-d)
- Understood relative vs absolute paths
- Introduced cron job scheduling
- Practiced log investigation (/var/log, journalctl)
- Debugged nginx using systemctl and logs
- Learned reload vs restart difference

### Mini Project – Nginx Log Monitor

Built a Bash script that:

- Reads nginx access log
- Counts total requests for today
- Counts 404 errors
- Calculates 404 error percentage
- Prints formatted daily report

Concepts Used:
- grep
- awk
- wc
- date
- conditional logic
- shell arithmetic

### API Integration
- Created Python virtual environment
- Installed requests safely
- Called GitHub public API
- Parsed JSON response
- Handled exceptions
