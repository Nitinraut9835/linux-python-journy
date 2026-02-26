# Day 04 – Logs & Troubleshooting Deep Practice

## journalctl Basics

- journalctl -n 10 → last 10 logs
- journalctl -f → live logs
- journalctl -u nginx → logs for specific service
- journalctl -p err → only error level logs
- journalctl --since today → logs from today

## Log Priorities

- emerg
- alert
- crit
- err
- warning
- notice
- info
- debug

## Authentication Logs

On this system, logs are stored in systemd journal (not /var/log/auth.log).

To check failed logins:
journalctl | grep "Failed password"

## Troubleshooting Workflow

When website is down:

1. systemctl status nginx
2. ss -tulnp | grep :80
3. curl localhost
4. Check firewall (ufw / iptables)
5. Check DNS
6. Check logs

## Network Thinking

If:
- curl localhost works
- IP works
- Domain fails

→ DNS issue

If:
- HTTP works
- HTTPS fails

→ Port 443 or SSL configuration issue

If:
- Listening on 127.0.0.1

→ Server only accessible locally

Should listen on 0.0.0.0 for external access
