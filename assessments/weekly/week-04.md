# Weekly Assessment: Week 04 — Networking Fundamentals II

**Assessment Type:** Saturday Live Evaluation & Technical Examination  
**Passing Score:** Minimum 80 / 100 points  
**Prerequisites:** All 5 weekly assignments (A04-01 to A04-05) submitted and validated.

---

## 1. 100-Point Evaluation Rubric

| Category | Max Points | Passing Bar | Evaluation Criteria |
|---|:---:|:---:|---|
| **1. Conceptual Understanding** | **20** | 16 | Explains the architecture of HTTP/1.1 and HTTP/2 protocol architecture and Client-server request and response lifecycle, operational tradeoffs, and protocol lifecycles without reading notes. |
| **2. Practical Implementation** | **40** | 32 | Code, scripts, or infrastructure using curl execute cleanly, meet all functional requirements, follow security baselines, and have zero syntax errors. |
| **3. Independent Problem Solving** | **20** | 16 | Successfully isolates, analyzes, and rectifies a live injected failure in curl within 30 minutes using structured diagnostic commands. |
| **4. Technical Documentation** | **10** | 8 | Provides clear Markdown documentation, reproduction steps, verification commands, and architecture diagrams. |
| **5. Consistency & Completion** | **10** | 8 | Completed on time, clean Git commits, zero secrets leaked, and structured weekly report submitted. |
| **Total** | **100** | **80** | **Aggregate Pass Threshold: >= 80/100** |

---

## 2. Part 1: Knowledge Assessment (Oral / Written)
The mentor asks the learner the following 5 technical questions. The learner must answer in their own words:
1. Explain the architectural role of HTTP/1.1 and HTTP/2 protocol architecture in modern cloud and DevOps environments.
2. What are the common failure modes associated with Client-server request and response lifecycle, and how do you monitor for them?
3. How does curl interact with underlying operating system resources (CPU, memory, networking, disk)?
4. Explain how the Principle of Least Privilege applies to HTTP/1.1 and HTTP/2 protocol architecture.
5. If a customer reports service degradation related to Networking Fundamentals II, what three diagnostic steps do you execute first?

---

## 3. Part 2: Practical Engineering Challenge
**Time Limit:** 60 minutes  
**Objective:** The learner must independently construct a working implementation demonstrating HTTP/1.1 and HTTP/2 protocol architecture and Client-server request and response lifecycle.
- Must run in an isolated environment.
- Must execute unattended.
- Must produce verifiable logs or metrics.
- Must include a clean teardown or cleanup mechanism.

---

## 4. Part 3: Independent Troubleshooting Task (Live Injected Failure)
**Time Limit:** 30 minutes  
**Scenario:** The mentor injects a specific operational defect into the learner's environment (e.g., misconfigured network port, permission violation, corrupted configuration syntax, or failing dependency).
**Learner Diagnostic Requirements:**
- The learner must share their terminal screen.
- The learner must verbalize their diagnostic reasoning using the 15-minute rule.
- The learner must inspect logs, identify the root cause, apply the fix, and verify recovery.

---

## 5. Part 4: Live Mentor Demonstration & Defense
The learner walks the mentor through their weekly assignment code:
- Why did you choose this specific configuration or architecture?
- Explain what happens under high load or when a network timeout occurs.
- The mentor instructs the learner to make one on-the-fly modification to verify code ownership.

---

## 6. Score Recording & Sign-off

```text
Learner Name: _______________________    Date: _______________
Mentor Name:  _______________________    Week: Week 04

[ ] Part 1: Conceptual Understanding     Score: ____ / 20
[ ] Part 2: Practical Implementation     Score: ____ / 40
[ ] Part 3: Independent Troubleshooting  Score: ____ / 20
[ ] Part 4: Technical Documentation      Score: ____ / 10
[ ] Part 5: Consistency & Completion     Score: ____ / 10
--------------------------------------------------------------
TOTAL SCORE:                             Score: ____ / 100

Status: [ ] PASS (>=80)   [ ] CONDITIONAL (70-79)   [ ] REASSESS (<70)

Mentor Signature: _____________________________________________
```
