# Mini-Project 1: Automated Linux System Health Monitor & Notifier

**Stage:** End of Stage 1 (Week 7 Milestone)  
**Technologies:** Bash, Python 3, Linux systemd, Cron, Slack/Webhook API

## Project Overview
Build an automated, production-ready system monitoring agent that runs on a Linux server, collects system telemetry (CPU, RAM, Disk, active SSH sessions, failed login attempts), and delivers structured alerts when thresholds are exceeded.

## Functional Requirements
1. **Telemetry Collector:** A Python daemon `monitor.py` collecting CPU %, memory %, disk utilization %, and load averages every 30 seconds.
2. **Threshold Alerting:** If CPU > 85%, RAM > 90%, or Disk > 85%, dispatch a formatted JSON alert via webhook.
3. **systemd Supervision:** Package as a systemd unit `healthmon.service` with auto-restart on failure, memory caps (`MemoryMax=100M`), and running as a dedicated system user `healthmon`.
4. **Log Auditing:** Rotate logs automatically via `/etc/logrotate.d/healthmon`.
