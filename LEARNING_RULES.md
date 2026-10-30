# Core Learning Rules & Code of Engineering Discipline

This programme is built on one governing principle: **real engineering competence is measured by what you can build, explain, and debug independently.**

---

## Rule 1: The 15-Minute Rule Before Asking for Help

When you encounter an error:
1. **Pause.** Read the error message carefully from the bottom up.
2. **Investigate.** Check logs, inspect network sockets, check permissions, or review the relevant man page/documentation.
3. **Try at least two distinct hypotheses** and document what happened.
4. If you remain stuck after 15 minutes of structured troubleshooting, raise a GitHub Blocker Issue using the [Blocker Template](.github/ISSUE_TEMPLATE/blocker.yml) or contact your mentor.
5. In your help request, you must state:
   - What you were trying to achieve.
   - The exact command run and complete error output.
   - What you hypothesized and tested.
   - Why you believe those attempts failed.

*Never ask: "It doesn't work, what should I do?"*

---

## Rule 2: Ethical & Responsible AI Usage

Generative AI (ChatGPT, Claude, Gemini, Copilot) is a common productivity tool in modern engineering. However, using AI to generate solutions you do not understand will actively prevent you from passing progression gates and technical interviews.

### Permitted AI Usage:
- Explaining confusing error messages or log traces.
- Socratic querying ("Can you explain how TCP window scaling works?").
- Reviewing code for potential edge cases after you have written it.
- Generating synthetic test data.

### Strictly Prohibited AI Usage:
- Prompting AI to generate complete assignment solutions or scripts.
- Copy-pasting code into assignments without line-by-line understanding.
- Submitting weekly reports authored by AI.

### The Explanation Rule:
If you submit code, **you are certifying that you can explain every single line, flag, and configuration parameter in a live terminal session.** If asked by your mentor to modify the script on the fly or explain a command flag you used and you cannot, the assignment will be invalidated and marked as 0.

---

## Rule 3: Zero Secret Commits (The Nuclear Rule)

Accidentally committing credentials (AWS Access Keys, Database Passwords, SSH Private Keys, API Tokens) to a Git repository is a critical security failure.

- Always verify `.gitignore` before `git add`.
- Use environment variables (`.env`) for local development, and never commit `.env` files.
- If a secret is committed:
  1. Immediately revoke and invalidate the secret at the provider (e.g., AWS Console).
  2. Inform your mentor immediately.
  3. Scrub the Git history using `git-filter-repo` or BFG Repo-Cleaner.

---

## Rule 4: Daily Documentation Habit

Documentation is not an afterthought; it is a primary deliverable of a DevOps engineer.
- Spend 30 minutes at the end of every study session recording notes in your personal engineering journal.
- Maintain accurate runbooks for every multi-step setup.
- Write READMEs that allow any engineer to clone your repository and reproduce your environment in under 5 minutes.

---

## Rule 5: Active Recall Over Passive Consumption

- Watching a video tutorial is not learning.
- Reading documentation is familiarization.
- **Typing commands, breaking configurations, and fixing them is learning.**
- Always build from memory first. When you look up syntax, close the documentation and type it out manually rather than copy-pasting.

---

## Rule 6: Respect Cloud Budgets

- Always verify the cost profile before launching cloud resources.
- Set up AWS CloudWatch Billing Alarms on Day 1 of cloud work.
- Run `terraform destroy` or terminate EC2 instances at the end of each study session unless persistent operation is explicitly required.
- Untracked running cloud resources will lead to suspension of cloud lab privileges.
