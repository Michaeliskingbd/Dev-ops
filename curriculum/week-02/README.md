# Week 02: Linux Fundamentals II

**Stage 1: Technical Foundations (Days 8-14)**

---

## 1. Week Number and Title
- **Week:** Week 02
- **Title:** Linux Fundamentals II
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 8 to 14

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master processes and process management and articulate its operational tradeoffs.
- Master services and systemd unit management and articulate its operational tradeoffs.
- Master package management (apt/dpkg) and articulate its operational tradeoffs.
- Master environment variables and shell configuration and articulate its operational tradeoffs.
- Master ssh and secure remote server access and articulate its operational tradeoffs.
- Master system logs and journalctl and articulate its operational tradeoffs.
- Master disk usage, partitions, and storage analysis and articulate its operational tradeoffs.
- Master basic linux server administration and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using systemd, systemctl, journalctl, ps/htop/top, OpenSSH, apt, df/du/lsblk.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Completion of Week 01 (Linux Fundamentals I) including command line navigation and permissions.

---

## 4. Why the Topic Matters in DevOps
In cloud environments, web servers, database engines, and background workers run as managed daemon processes. A DevOps engineer must know how to inspect resource-hungry processes, configure systemd unit files with restart policies, manage system packages securely, configure SSH hardening, and analyze journalctl logs during outages.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Process Lifecycle and Process Management
In Linux, every running program is represented as a **Process** with a unique Process ID (`PID`).
- The initial user-space process spawned by the kernel is `systemd` (PID 1).
- Processes exist in states: Running (`R`), Sleeping (`S`), Uninterruptible Disk Sleep (`D`), Stopped (`T`), or Zombie (`Z` - terminated child waiting for parent to read exit status).
- Signal Handling: `SIGTERM` (15) requests graceful termination; `SIGKILL` (9) forcefully terminates without cleanup; `SIGHUP` (1) signals configuration reload.

### 2. Service Management with systemd
Modern Linux distributions use **systemd** as their init system and service supervisor.
- A **Unit file** (e.g., `/etc/systemd/system/myapp.service`) describes how to launch, supervise, restart, and sandbox a daemon.
- Key directives: `[Unit]` (metadata & dependencies), `[Service]` (execution command, user, restart policy, resource limits), and `[Install]` (target milestone, e.g., `multi-user.target`).
- Commands: `systemctl start`, `systemctl stop`, `systemctl restart`, `systemctl status`, `systemctl enable` (create symlink in target), `systemctl daemon-reload`.

### 3. SSH Architecture and Server Hardening
Secure Shell (SSH) is the ubiquitous protocol for remote Linux server administration.
- Configuration resides in `/etc/ssh/sshd_config`.
- Production security standards: Disable password authentication (`PasswordAuthentication no`), disable root remote login (`PermitRootLogin no`), enforce public-key authentication (`PubkeyAuthentication yes`), and use modern elliptic curve cryptography (Ed25519).

### 4. Storage and Storage Analysis
- `df -h`: Inspects filesystem disk space utilization.
- `du -sh /var/*`: Calculates disk usage of specific directories.
- `lsblk`: Displays block storage devices, partitions, and mount points.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 8):** Process hierarchy, PID 1, inspecting running processes with `ps aux`, `ps -ef --forest`, real-time monitoring with `htop` / `top`, and sending process signals with `kill` and `pkill`.
- **Tuesday (Day 9):** systemd architecture: unit files, service lifecycles, creating a custom background Python daemon, writing a custom `.service` file, testing restart policies (`Restart=on-failure`), and reloading with `systemctl daemon-reload`.
- **Wednesday (Day 10):** Package management deep dive (`apt update`, `apt upgrade`, `apt install`, inspecting package contents with `dpkg -L`, removing unused dependencies with `apt autoremove --purge`), and environment variable persistence (`/etc/environment`, `~/.bashrc`).
- **Thursday (Day 11):** SSH architecture: generating Ed25519 key pairs (`ssh-keygen -t ed25519`), copying keys via `ssh-copy-id`, hardening `/etc/ssh/sshd_config`, configuring `~/.ssh/config` profiles, and testing connection logs.
- **Friday (Day 12):** Centralized logging & storage forensics: inspecting `/var/log`, filtering systemd journal logs using `journalctl -u service -f --since "1 hour ago" -p err`, and diagnosing disk usage bottlenecks using `df -h` and `du -sh`.
- **Saturday (Day 13):** Practical engineering challenge: Deploy a resilient background metric-collector daemon managed by systemd, configure log rotation, restrict execution to an unprivileged system account, and harden remote SSH access.

---

## 7. Practical Terminal Exercises
```bash
# 1. Process inspection and tree visualization
ps -eo pid,ppid,user,%cpu,%mem,cmd --sort=-%cpu | head -n 10
pstree -p

# 2. Inspect systemd service states
systemctl list-units --type=service --state=running
systemctl status sshd.service

# 3. Create an isolated system daemon user
sudo useradd --system --no-create-home --shell /usr/sbin/nologin appdaemon

# 4. Filter system logs for errors
sudo journalctl -p 3 -xb --no-pager | tail -n 30

# 5. Storage analysis
df -hT
sudo du -ah /var/log | sort -rh | head -n 10
lsblk -f
```

---

## 8. Realistic Engineering Scenarios
**Scenario: The Mystery CPU Spike & Zombie Outage**
A production web server becomes unresponsive every evening. Monitoring shows CPU pegged at 100% and disk space on `/var/log` exhausted. An unmonitored background script is forking child processes that crash immediately without their exit status being reaped, accumulating thousands of zombie processes and writing gigabytes of unrotated stack traces.
*The DevOps Task:* Identify the offending parent process, terminate it gracefully, configure a systemd service wrapper with memory/CPU limits (`MemoryMax=500M`, `CPUQuota=50%`), and establish log rotation via `logrotate`.

---

## 9. Common Mistakes
- **Modifying system unit files in `/lib/systemd/system/` instead of `/etc/systemd/system/`:** Vendor packages overwrite `/lib/systemd/system/` during updates. Custom configs and overrides must always be placed in `/etc/systemd/system/`.
- **Forgetting `systemctl daemon-reload`:** Changes to `.service` files on disk are ignored by systemd until the daemon re-reads configuration files.
- **Locking oneself out of SSH during hardening:** Always test SSH configuration changes in a second terminal session (`ssh -i key user@host`) *before* closing your existing active connection.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a CrashLooping systemd Service**
1. **Symptom:** `systemctl status customapp.service` reports `Active: activating (auto-restart) (Result: exit-code)`.
2. **Diagnostic commands:**
   ```bash
   # Inspect the full failure trace
   sudo journalctl -u customapp.service -n 50 --no-pager -e
   # Verify executable permissions and shebang
   ls -la /usr/local/bin/customapp
   # Run the command manually as the service user
   sudo -u appdaemon /usr/local/bin/customapp
   ```
3. **Common Causes:** Missing executable bit (`chmod +x`), environment variable not set in systemd unit, or service user lacking read permissions to configuration files.
4. **Resolution:** Add `EnvironmentFile=/etc/customapp.env` to the service unit and ensure file permissions are owned by `appdaemon`.

---

## 11. Required Tools and Installation Instructions
```bash
# Ubuntu / Debian
sudo apt-get update && sudo apt-get install -y \
    systemd \
    openssh-server \
    logrotate \
    htop \
    psmisc
```

---

## 12. Official Documentation and Reliable Learning Resources
- [systemd System and Service Manager](https://systemd.io/)
- [systemd.service Documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [OpenSSH Official Documentation](https://www.openssh.com/manual.html)
- [Debian Wiki - Package Management](https://wiki.debian.org/Apt)

---

## 13. Expected Weekly Deliverables
1. Production-ready systemd unit file with resource limits and restart policies.
2. Hardened `sshd_config` with validation log.
3. Solutions to Assignments A02-01 through A02-05 in `submissions/week-02/`.
4. Weekly Progress Report in `weekly-reports/week-02-report.md`.

---

## 14. Knowledge-Check Questions
1. What is the fundamental difference between `SIGTERM` (15) and `SIGKILL` (9)? Which should be used first and why?
2. Explain the purpose of `Restart=on-failure` versus `Restart=always` in a systemd service unit.
3. What is a zombie process? How do you clear zombie processes from the process table?
4. Explain why public-key authentication (Ed25519) is cryptographically superior to password authentication for SSH.
5. What is the difference between `df` and `du`, and why might `df` report a disk as full while `du` shows free space?

---

## 15. Weekly Practical Challenge
Build a custom Python telemetry daemon `sysmonitor.py` that collects memory, disk, and load metrics every 10 seconds. Package it into a systemd service `sysmonitor.service` that runs as a dedicated unprivileged user, restarts automatically within 5 seconds if crashed, caps memory at 128MB via `MemoryMax`, and forwards structured logs to journald.

---

## 16. Assessment Criteria
Conceptual: 20 pts | Implementation: 40 pts | Troubleshooting: 20 pts | Documentation: 10 pts | Timeliness: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100, custom systemd service functional and verified in journald, SSH key hardening verified without lockout.
