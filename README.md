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

### Day 04
- Deep log analysis using journalctl
- Learned log priorities and filtering
- Practiced authentication log monitoring
- Built structured troubleshooting workflow
- Understood network vs service vs DNS issues
- Learned HTTP vs HTTPS debugging logic

### Mini Project – Nginx Reverse Proxy Lab

Built a production-style reverse proxy setup:

- Configured Nginx as a reverse proxy to a Python backend
- Implemented backend service on port 5000
- Tested HTTP responses (200, 404, 500)
- Simulated backend failure to generate 502 Bad Gateway
- Analyzed access and error logs
- Investigated service failures using systemctl and journalctl
- Practiced reload vs restart behavior

Concepts Used:

- Reverse proxy architecture
- HTTP status codes
- Linux log analysis
- Service management (systemd)
- curl-based endpoint testing
- Basic incident troubleshooting

### Day 05
- Learned Docker fundamentals
- Understood image vs container
- Compared containers with VMs
- Installed Docker on Ubuntu
- Ran first container (hello-world)
- Deployed nginx inside container
- Practiced port mapping
- Understood host binding and network accessibility

### Day 06

- Built first Docker image and ran container successfully
