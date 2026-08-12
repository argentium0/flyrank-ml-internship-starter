# Future Case Study Expansion Plan & Reminders

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** Build (core) — The Plan to Keep Building (Adding future case studies & reminders)

---

## 1. Technical Recipe: How to Add the Next Case Study

To prevent the portfolio from going stale, future case studies will follow a repeatable, structured 3-beat layout. 

### **Step-by-Step Code Workflow:**

1. **Create the Case Study Page:**
   - Duplicate `case_study.html` and save it as `case_study_2.html` in the workspace root.
   - Replace the headers, title, and body elements with the new case text while preserving the base navigation header, styles, and footer components.

2. **Draft the 3-Beat Content Structure:**
   * **Beat 1 (The Problem):** Define the search intelligence friction (e.g. click-attribution latency, keyword cannibalization under global core updates).
   * **Beat 2 (What I Did):** Outline the technical methodology (e.g. DuckDB data window grouping, training an XGBoost classifier, validating out-of-sample).
   * **Beat 3 (What Came of It):** Document the quantitative result (e.g. +22% click recovery lift on holdout clients, precision comparison matrix) and action playbook recommendations.

3. **Link to Homepage Grid:**
   - In `index.html`, copy the existing card block in the **Featured Capstone Work** section and paste it right underneath.
   - Update the metrics, summary, tag, and change the CTA link button to point to `case_study_2.html`.

4. **Deploy & Push:**
   - Stage, commit, and push the updates:
     ```bash
     git add index.html case_study_2.html
     git commit -m "PF-07 Expansion: Add Case Study #2 — [Brief Title]"
     git push origin main
     ```

---

## 2. Named Future Project: "Autonomous MCP GSC Triage Agent"

* **The Goal:** Build an autonomous search intelligence agent using the Model Context Protocol (MCP).
* **The Method:** The agent connects to a local GSC warehouse via DuckDB, listens to search performance threshold alerts, and automatically generates audit recommendations for stale pages.
* **The Deliverable:** A command-line script + a dedicated case study page (`case_study_2.html`) demonstrating zero-leakage out-of-sample ranking.

---

## 3. Portfolio Review Reminder

* **The Reminder Action:** Setting a calendar alarm and recurring task in Notion for **September 15, 2026** (approx. 4 weeks post-launch) to review data pipeline logs and draft Case Study #2.
* **Agent Scheduled Reminder:** Active schedule task set to alert the review board for periodic audit checks.
