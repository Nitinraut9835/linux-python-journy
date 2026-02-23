# Day 02 – Linux Services

## What is a Service?
A background program that starts automatically and provides system functionality.

## What is systemd?
The service manager in modern Linux systems. It starts, stops, and monitors services.

## Important Concepts
- PID 1 = systemd
- start → runs service immediately
- enable → starts service automatically at boot
- systemd monitors services and can restart them

## Commands Practiced
- systemctl status
- systemctl list-units
- ps -p 1

## Key Understanding
- start/stop affect current state
- enable/disable affect boot state
- running state and boot configuration are independent
