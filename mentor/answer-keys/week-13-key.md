# Mentor Answer Key & Solution Guide: Week 13 — AWS Fundamentals I

> **CONFIDENTIAL — MENTOR USE ONLY**  
> Do not distribute or expose this document to learners.

---

## 1. Knowledge Check Solutions & Rubric

### Question 1: Explain the architectural role and core problem solved by Cloud computing service models (IaaS, PaaS, SaaS) and shared responsibility model.
**Expected Answer:**
- Clear definition of the technology and its place in the modern delivery lifecycle.
- Explains why manual or legacy approaches fail at scale.
- Discusses operational boundaries, performance tradeoffs, and security isolation.
*Grading Guide: Full 4 points if the learner explains operational tradeoffs without reciting textbook definitions.*

### Question 2: What are common operational failure modes in AWS Global Infrastructure: Regions, Availability Zones (AZs), and Edge Locations?
**Expected Answer:**
- Identifies misconfigurations (e.g., resource exhaustion, bad permissions, connection timeouts).
- Explains how these failures manifest in logs and metric alerts.
- Describes automated prevention strategies (e.g., healthchecks, retries, circuit breakers).

### Question 3: How does AWS Management Console interact with underlying system resources?
**Expected Answer:**
- Discusses socket bindings, filesystem descriptors, memory/CPU allocation, and process management.

---

## 2. Injected Failure Scenario (Saturday Assessment Drill)

### Scenario Setup:
The mentor introduces a deliberate defect into the learner's test environment:
```bash
# Injection command (mentor executes before assessment):
# Simulates a configuration breakage or permission violation
chmod 000 ~/devops-lab/week-13/config.env 2>/dev/null || true
```

### Expected Learner Diagnostic Workflow:
1. Learner attempts to start or query the service and observes the failure.
2. Learner inspects recent logs (`journalctl`, `docker logs`, or application error logs).
3. Learner identifies "Permission Denied" or "Connection Refused" rather than randomly guessing.
4. Learner verifies file permissions using `ls -la` or network listening sockets using `ss -tulpn`.
5. Learner rectifies the root cause and demonstrates healthy operational state.

*Scoring: Full 20 points if solved within 15 minutes with methodical reasoning.*

---

## 3. Assignment Reference Implementations & Expected Outputs
Mentor reference files for reviewing Assignments A13-01 through A13-05:
- Verify that learners did not hardcode values.
- Verify that error handling and exit codes are implemented.
- Check that all created resources are cleanly cleaned up after execution.
