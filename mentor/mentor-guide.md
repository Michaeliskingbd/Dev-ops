# Mentor Operating Playbook: Remote Supervision & Coaching

This operating guide defines the remote supervision cadence, pedagogical standards, and evaluation protocols for mentors guiding learners through the 180-Day DevOps Engineering Mentorship Programme.

---

## 1. Weekly Supervision Cadence

```text
┌───────────┬──────────────────────────────────────────────────────────────────┐
│ Day       │ Mentor Responsibility                                            │
├───────────┼──────────────────────────────────────────────────────────────────┤
│ Monday    │ Kickoff Sync (15 mins): Clarify weekly learning objectives,      │
│           │ highlight tricky concepts, and set deliverable expectations.     │
├───────────┼──────────────────────────────────────────────────────────────────┤
│ Wednesday │ Mid-Week Check-in: Review branch commits. Identify blocked      │
│           │ learners. Provide Socratic hints without giving away solutions. │
├───────────┼──────────────────────────────────────────────────────────────────┤
│ Friday    │ Pre-Review Pull Requests: Verify local test validation, check   │
│           │ for zero secret leaks, and flag incomplete assignments.          │
├───────────┼──────────────────────────────────────────────────────────────────┤
│ Saturday  │ Live Assessment Session (60–90 mins per learner):                │
│           │ • Oral knowledge check (20 pts)                                  │
│           │ • Practical challenge evaluation (40 pts)                        │
│           │ • Live failure injection troubleshooting drill (20 pts)          │
│           │ • Documentation review (10 pts)                                  │
│           │ • Record formal score in assessment sheet.                       │
├───────────┼──────────────────────────────────────────────────────────────────┤
│ Sunday    │ Audit weekly reports, update learner progress dashboard, and     │
│           │ finalize next week's kickoff notes.                              │
└───────────┴──────────────────────────────────────────────────────────────────┘
```

---

## 2. Socratic Questioning Techniques

A mentor does not solve problems for the learner. A mentor asks the questions that enable the learner to formulate the solution themselves.

### Effective Socratic Prompts:
- *"What does the kernel / network socket / Docker daemon see at this exact moment?"*
- *"If you inspect `ss -tulpn`, which process is holding port 5432?"*
- *"What happens to this data when the container is terminated and recreated?"*
- *"Why did you choose this specific flag rather than the alternative?"*
- *"If this traffic spikes by 100x, where does the architecture fail first?"*

---

## 3. Distinguishing Genuine Understanding from Tutorial-Copying and AI Abuse

In the age of LLMs and internet tutorials, learners can easily produce code that looks correct without understanding how it works.

### Detection Guidelines:
1. **The Modification Drill:**
   Instruct the learner during the live Saturday session to modify their code or configuration on screen:
   - *"Change this Nginx reverse proxy to proxy requests from `/api/v2` instead of `/api`."*
   - *"Modify this Bash script to log errors to syslog rather than a file."*
   - *"Add a readiness probe checking an HTTP endpoint rather than a TCP socket."*
   *If the learner wrote and understands the code, they can make these adjustments in under 3 minutes. If they copied an AI response or tutorial without understanding, they will struggle or stall.*

2. **The Command Flag Interrogation:**
   Point to flags in their scripts or commands:
   - *"What does `-euo pipefail` do in your Bash script? What happens if you remove `pipefail`?"*
   - *"What does `-p` do in `mkdir -p`?"*
   - *"What is the difference between `EXPOSE` and `-p 8080:8080` in Docker?"*

3. **Log Tracing Explanation:**
   Show them an error log from their own execution and ask them to explain the sequence of events from client initiation to connection termination.

---

## 4. Remediation Workflow

When a learner scores between 70 and 79 (Conditional Pass):
1. Identify the specific sub-topic where competency was missing (e.g., DNS resolution, Docker volumes, Terraform remote state).
2. Assign a targeted remedial exercise from `mentor/answer-keys/` with a 5-day deadline.
3. Conduct a 20-minute re-test before clearing the learner to proceed.
