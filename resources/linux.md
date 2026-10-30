# Linux Systems Administration & Architecture

> Essential reference guide for Linux system internals, command-line mastery, process supervision, storage administration, and server administration.

---

## 1. Verified Official Documentation & Standards
- [Linux Foundation Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/manual/)
- [systemd System & Service Manager](https://systemd.io/)
- [Debian / Ubuntu Administrator's Handbook](https://debian-handbook.info/)
- [ArchWiki Linux Administration Reference](https://wiki.archlinux.org/)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# Process & Resource Management
ps aux --sort=-%mem | head -n 15        # Top 15 memory-consuming processes
pstree -p                              # Process hierarchy with PIDs
kill -15 <PID>                         # Graceful SIGTERM
kill -9 <PID>                          # Forceful SIGKILL
kill -1 <PID>                          # SIGHUP (reload config)

# systemd Service Management
systemctl daemon-reload                # Reload unit files from disk
systemctl status <service>             # Inspect service health and logs
systemctl restart <service>            # Restart daemon
journalctl -u <service> -f --since "1h" # Real-time filtered logs

# Storage & Filesystem
df -hT                                 # Filesystem disk usage and types
du -sh /var/* | sort -rh | head -n 10   # Top 10 largest folders in /var
lsblk -f                               # Block devices and UUIDs
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.
