# Week 01: Linux Fundamentals I

**Stage 1: Technical Foundations (Days 1-7)**

---

## 1. Week Number and Title
- **Week:** Week 01
- **Title:** Linux Fundamentals I
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 1 to 7

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master linux distributions and architecture and articulate its operational tradeoffs.
- Master terminal and shell fundamentals and articulate its operational tradeoffs.
- Master filesystem hierarchy (fhs) and articulate its operational tradeoffs.
- Master navigation and file manipulation and articulate its operational tradeoffs.
- Master file permissions and ownership and articulate its operational tradeoffs.
- Master users and groups management and articulate its operational tradeoffs.
- Master core command-line utilities and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Bash, Ubuntu/Debian, coreutils, chmod/chown, useradd/usermod.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
A computer with terminal access (Ubuntu Linux, macOS, or Windows WSL2 with Ubuntu). No prior Linux experience required.

---

## 4. Why the Topic Matters in DevOps
Over 90% of public cloud instances, container images, and production servers run on Linux. If you cannot navigate the Linux filesystem, inspect permissions, and manage user boundaries from the terminal without a graphical user interface, you cannot automate, containerize, or secure cloud infrastructure.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. The Linux Kernel vs Distribution
The **Linux kernel** is the core software that manages CPU, memory, storage devices, and hardware interrupts. A **Linux distribution** (distro) combines the Linux kernel with standard GNU utilities, a package manager (e.g., `apt` for Debian/Ubuntu, `dnf` for RHEL/CentOS), system libraries, and default configurations. In enterprise DevOps, Ubuntu LTS and Red Hat Enterprise Linux (RHEL) / Rocky Linux dominate production environments.

### 2. The Linux Filesystem Hierarchy Standard (FHS)
Unlike Windows which uses drive letters (`C:\`, `D:\`), Linux represents everything under a single unified root directory: `/`.
- `/bin` & `/usr/bin`: Essential user command binaries (e.g., `ls`, `grep`, `cat`).
- `/etc`: Host-specific system-wide configuration files (e.g., `/etc/nginx`, `/etc/ssh/sshd_config`, `/etc/passwd`).
- `/var`: Variable data files, including application logs (`/var/log`), spool directories, and temporary state.
- `/home`: User personal directories (e.g., `/home/devops/`). Root user's home is `/root`.
- `/dev`: Device nodes representing hardware interfaces (e.g., disks like `/dev/nvme0n1` or `/dev/sda`).
- `/proc` & `/sys`: Virtual pseudo-filesystems exposing kernel parameters and process states in real-time.

### 3. File Permissions and Ownership Model
Every file and directory in Linux has an **Owner User (u)**, an **Owner Group (g)**, and **Others (o)**.
Permissions are divided into three basic capabilities:
- **Read (r = 4):** View file contents or list directory entries.
- **Write (w = 2):** Modify file contents or create/delete files within a directory.
- **Execute (x = 1):** Execute a binary/script, or traverse (`cd`) into a directory.
- **Special Permissions:** SUID (4000), SGID (2000), and Sticky Bit (1000 - e.g., `/tmp`).

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 1):** Terminal anatomy, shell concepts, SSH login into a Linux host, navigation (`pwd`, `cd`, `ls -lah`), relative vs absolute paths.
- **Tuesday (Day 2):** File operations: creating files (`touch`), directories (`mkdir -p`), copying (`cp -r`), moving/renaming (`mv`), deleting (`rm -rf`), and viewing files (`cat`, `less`, `head`, `tail -n 20`).
- **Wednesday (Day 3):** User & group administration: inspecting `/etc/passwd`, `/etc/group`, `/etc/shadow`, creating users with `useradd -m -s /bin/bash`, modifying groups with `usermod -aG`, and understanding `sudo` privileges via `/etc/sudoers`.
- **Thursday (Day 4):** Permission mechanics: understanding numeric (octal) vs symbolic notation (`chmod 750`, `chmod u+rwx,g+rx,o-rwx`), changing ownership (`chown user:group`), and directory execution semantics.
- **Friday (Day 5):** Text stream processing & core utilities: pipes (`|`), standard streams (stdin `0`, stdout `1`, stderr `2`), redirection (`>`, `>>`, `2>&1`), searching with `grep -rnI`, counting with `wc -l`, sorting with `sort | uniq -c`, and finding files with `find /var/log -name "*.log" -mtime -7`.
- **Saturday (Day 6):** Practical engineering challenge: Hardening an enterprise multi-tier project directory tree with isolated team group permissions, sticky bits, and an automated permission verification script.

---

## 7. Practical Terminal Exercises
```bash
# 1. Inspect Linux distribution and kernel details
uname -a
cat /etc/os-release

# 2. Explore the Filesystem Hierarchy
ls -ld / /bin /etc /var /proc /dev

# 3. Create a structured project directory tree
mkdir -p ~/devops-lab/{web,api,db,logs}
touch ~/devops-lab/web/index.html ~/devops-lab/api/app.py ~/devops-lab/logs/access.log

# 4. Create dedicated users and groups
sudo groupadd -g 2001 devops-team
sudo groupadd -g 2002 audit-team
sudo useradd -m -u 1001 -g devops-team -s /bin/bash engineer_alice
sudo useradd -m -u 1002 -g audit-team -s /bin/bash auditor_bob

# 5. Configure ownership and permissions
sudo chown -R engineer_alice:devops-team ~/devops-lab
chmod -R 750 ~/devops-lab
chmod 770 ~/devops-lab/logs

# 6. Stream redirection and text filtering
find /etc -maxdepth 2 -type f 2>/dev/null | grep -E "(ssh|ssl)" | wc -l
```

---

## 8. Realistic Engineering Scenarios
**Scenario: The Runaway Shared Directory Breach**
In an engineering organization, developers and auditors shared a `/opt/deployments` directory. A developer inadvertently ran `chmod -R 777 /opt/deployments`, allowing any user on the system to overwrite sensitive deployment configuration scripts. Furthermore, junior engineers were deleting each other's temporary test files because the directory lacked the Sticky Bit.
*The DevOps Task:* Audit permissions across `/opt/deployments`, enforce group-based ownership (`deploy-team`), strip world-writable permissions, and apply the Sticky Bit (`chmod +t`) so users can only delete their own files.

---

## 9. Common Mistakes
- **Running `rm -rf /path /to/dir` with an accidental space:** Typing `rm -rf / path/to/dir` can wipe the root filesystem. Always double-check paths before running `rm -rf`.
- **Confusing directory read (`r`) and execute (`x`) permissions:** Setting `chmod 644` on a directory makes it un-traversable (`cd` will fail with Permission Denied) because directory navigation requires the execute (`x`) bit.
- **Editing `/etc/sudoers` directly with `nano`:** Always use `sudo visudo`, which validates syntax before saving to prevent permanently locking yourself out of administrative privileges.

---

## 10. Troubleshooting Exercises
**Exercise: Resolving "Permission Denied" for an Application Service Account**
1. **Symptom:** The service account `appuser` cannot read `/var/log/customapp/audit.log`.
2. **Diagnostic commands:**
   ```bash
   # Check file ownership and octal permissions
   ls -ld /var/log/customapp /var/log/customapp/audit.log
   # Check groups of the user
   id appuser
   # Test user permission simulation
   sudo -u appuser cat /var/log/customapp/audit.log
   ```
3. **Root Cause Analysis:** Even if `audit.log` has `rw-r--r--` (read for all), if `/var/log/customapp` has permissions `750` (`rwxr-x---`) owned by `root:adm`, and `appuser` is not a member of `adm`, `appuser` cannot traverse the parent directory.
4. **Resolution:** Add `appuser` to the `adm` group (`sudo usermod -aG adm appuser`) or adjust parent directory group permissions appropriately.

---

## 11. Required Tools and Installation Instructions
```bash
# Ubuntu / Debian
sudo apt-get update && sudo apt-get install -y \
    bash-completion \
    coreutils \
    tree \
    curl \
    htop \
    man-db
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Linux Foundation FHS 3.0 Specification](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)
- [Ubuntu Server Guide - User Management](https://ubuntu.com/server/docs/security-users)
- [ArchWiki File Permissions & Attributes](https://wiki.archlinux.org/title/File_permissions_and_attributes)

---

## 13. Expected Weekly Deliverables
1. Multi-tier directory structure script with verified permissions.
2. User and group audit documentation.
3. Solutions and terminal logs for Assignments A01-01 through A01-05 in `submissions/week-01/`.
4. Completed Weekly Progress Report in `weekly-reports/week-01-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the difference between the hard link and a symbolic (soft) link in the Linux filesystem.
2. What happens to directory navigation when a directory has read (`r`) permission but lacks execute (`x`) permission?
3. What is the octal representation of a file with permissions `-rwxr-s---`? Explain the purpose of the SetGID bit on a directory.
4. Why is `/etc/shadow` only readable by the `root` user, while `/etc/passwd` is world-readable?
5. How does `2>&1` work in shell stream redirection?

---

## 15. Weekly Practical Challenge
Create a Bash script `harden_app_directory.sh` that takes a directory path and group name as parameters, validates that the group exists, applies least-privilege permissions (`750` for directories, `640` for files), sets the Sticky Bit on a nested `tmp/` directory, and outputs a formatted audit table of all files violating the security baseline.

---

## 16. Assessment Criteria
Conceptual: 20 pts | Implementation: 40 pts | Troubleshooting: 20 pts | Documentation: 10 pts | Timeliness: 10 pts.

---

## 17. Progression Requirements
Must achieve score >= 80/100, pass all syntax and permission checks, and successfully demonstrate manual user creation and permission debugging live with the mentor.
