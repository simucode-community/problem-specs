# Contributing to SimuCode Problem Specs

Thank you for helping improve SimuCode's problem library.  
This guide tells you exactly what to contribute and how.

---

## What this repo is

This repo contains the **open specifications** for every problem on [simucode.online](https://simucode.online):
- Problem descriptions (`spec.md`)
- Starter code (`starter.py`)
- Hints (`hints.json`)

TestScripts (the grading logic) and reference solutions are **not** in this repo.  
That's intentional — it keeps grading integrity intact.

---

## Types of contributions

### 1. Fix an existing problem spec

**Examples:**
- Typo or grammatical error in `spec.md`
- Requirement is ambiguous or contradicts the starter code
- A hint is misleading or could be clearer
- A link in the spec is broken

**How to do it:**
1. Find the problem in `problems/` (e.g. `problems/001-simple-publisher/`)
2. Edit `spec.md` or `hints.json`
3. Open a Pull Request — title: `fix(001): [short description]`
4. In the PR body, explain what was wrong and what you changed

---

### 2. Suggest a new problem

Don't open a PR for new problems — open a Discussion instead.

👉 [New Problem Idea Discussion Template](https://github.com/simucode-community/problem-specs/discussions/new?category=problem-ideas)

Fill in:
```
**Problem Title:** 
**ROS2 Concept it tests:** 
**Difficulty:** Easy / Medium / Hard
**Why this problem matters:**
**Which companies ask this:**
**Example — what a student writes:**
**Example — what the node should do:**
```

The SimuCode team will:
1. Review the idea (within 1 week)
2. Label it `accepted` or `needs-discussion`
3. Build the testScript and deploy it to simucode.online
4. Add "Suggested by @username" to the problem page

---

### 3. Report a bug

If a problem's testScript fails on code you believe is correct — report it.

👉 [Bug Report Discussion Template](https://github.com/simucode-community/problem-specs/discussions/new?category=bug-reports)

Include:
```
**Problem ID and title:**
**What happened:** [testScript said FAILED]
**What I expected:** [testScript should say PASSED]
**My code:** (paste your solution — it won't appear to other users until you share it)
**ROS2 version:** Humble
```

---

### 4. Share your solution approach

After solving a problem, share how you approached it.

👉 [Show & Tell](https://github.com/simucode-community/problem-specs/discussions/categories/show-tell)

Don't paste full solutions — share the approach, the edge cases you hit, what clicked.

---

## Pull Request rules

| Rule | Why |
|------|-----|
| Only edit `spec.md` or `hints.json` | We maintain starter.py for consistency |
| One problem per PR | Easier to review |
| Title format: `fix(001): description` | Keeps history clean |
| No solutions in PRs | Preserves integrity |

---

## Code of Conduct

Be helpful. Be specific. Be kind.  
This is a learning community — treat everyone as a beginner until proven otherwise.

Questions? Open a [Q&A Discussion](https://github.com/simucode-community/problem-specs/discussions/categories/q-a).
