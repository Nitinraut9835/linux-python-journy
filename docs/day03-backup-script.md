# Day 03 - Bash Backup Script

## What This Script Does
- Takes a directory as input
- Checks if it exists
- Creates timestamped backup folder
- Copies directory using cp -r

## Key Concepts Learned
- $1 (positional argument)
- -z (empty check)
- -d (directory check)
- $(date)
- Relative vs Absolute paths
- Executable permissions


## Part 2 – Cron & Log Debugging

### Cron

- crontab -l → list jobs
- crontab -e → edit jobs
- Cron runs commands automatically at scheduled times
- Format: * * * * * command
- Always use absolute paths in cron
- Use >> to append logs
- Avoid overlapping long-running jobs

### Logs

- /var/log → stores system & application logs
- journalctl -u nginx → check nginx service logs
- /var/log/nginx/error.log → application errors
- /var/log/nginx/access.log → HTTP requests

### Debugging Flow Learned

1. systemctl status nginx
2. journalctl -u nginx -n 50
3. nginx -t
4. Fix config
5. reload instead of restart (safer)
