# Programme Assessment & Evaluation Policy

The evaluation system in this programme is designed to ensure genuine engineering competency. Advancing to subsequent stages requires verifiable evidence of independent technical problem-solving.

---

## 1. The 100-Point Weekly Assessment Rubric

Each week, the learner is scored against a standardised 100-point rubric:

| Category | Points | Description & Evaluation Standard |
|---|:---:|---|
| **1. Conceptual Understanding** | **20** | Ability to explain underlying system architecture, network protocols, tool mechanics, and design tradeoffs without reading from notes. |
| **2. Practical Implementation** | **40** | Code, configuration, scripts, or infrastructure are syntactically clean, robust, secure, and fully functional according to specifications. |
| **3. Independent Problem Solving** | **20** | Ability to diagnose an injected failure, trace logs, isolate the root cause, and rectify the issue without mentor spoon-feeding. |
| **4. Technical Documentation** | **10** | High-quality Markdown documentation, clear architecture diagrams, reproducible commands, and complete runbooks. |
| **5. Consistency & Completion** | **10** | On-time submission of all 5 weekly assignments, clean Git commits, and structured weekly progress report. |
| **Total** | **100** | **Passing Benchmark: 80 / 100** |

---

## 2. Grading Scale & Outcomes

- **80 – 100 Points: Full Pass**
  - All critical practical requirements are satisfied.
  - Learner demonstrates clear technical autonomy.
  - Eligible to proceed to next week.
- **70 – 79 Points: Conditional Pass**
  - Core concepts understood, but gaps exist in edge-case handling, error handling, or troubleshooting.
  - Learner must submit a remedial correction task within 5 business days.
- **60 – 69 Points: Reassessment Required**
  - Major practical requirements failed or learner was unable to explain implemented code.
  - Learner must spend 3 days reviewing curriculum and sit for a re-examination.
- **Below 60 Points: Unsatisfactory / Repeat Week**
  - Foundational prerequisites missing.
  - The week must be repeated in full before re-evaluation.

> [!WARNING]
> **The Critical Requirement Rule:**
> A score of 80+ does **not** grant a pass if any critical practical safety requirement is breached (e.g., committing plain-text AWS secret keys, failing to configure security groups, or failing to run database migrations).

---

## 3. Competency Progression Tiers

Every skill in the programme is tracked across five competency states:

1. `NOT_STARTED`: Topic has not yet been introduced.
2. `LEARNING`: Actively studying documentation and completing initial exercises.
3. `GUIDED`: Capable of completing tasks with mentor guidance or reference templates.
4. `INDEPENDENT`: Capable of designing, implementing, and debugging solutions autonomously without assistance.
5. `NEEDS_REASSESSMENT`: Previously demonstrated skill shows degradation during integrated milestone drills.

*Only skills marked `INDEPENDENT` count toward Progression Gate qualification.*

---

## 4. Formal Progression Gates

Progression Gates occur at the conclusion of each stage:
- **Gate 1 (End of Week 8):** Systems, Networks, Git, Python, and Database Architecture.
- **Gate 2 (End of Week 16):** Containers, CI/CD, AWS Cloud, and Terraform Infrastructure as Code.
- **Gate 3 (End of Week 24):** Kubernetes, Observability, DevSecOps, SRE, and Capstone Project Defense.

### Gate Passing Protocol
1. **Written Technical Exam (45 mins):** 20 comprehensive questions covering systems design and protocols.
2. **Live Hands-On Troubleshooting Scenario (60 mins):** The mentor presents a broken environment (e.g., broken Nginx upstream, bad routing table, failing pod, terraform state lock) which the learner must diagnose and resolve live on screen.
3. **Architecture Defense (30 mins):** Socratic interrogation where the learner defends their code and infrastructure decisions.
4. **Mentor Unanimous Sign-Off:** Required before learner can advance to the next stage.
