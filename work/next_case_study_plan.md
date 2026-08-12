# How to Add the Next Case Study: Expansion Plan & Reminder Log

**Project:** Ahsan's Search Intelligence Portfolio  
**Track:** Applied Search Intelligence  

---

## 1. Technical Recipe: How to Add a New Case Study

Future case studies will follow a repeatable 3-beat structure. Follow these technical steps:

1. **Create the Page:**
   - Duplicate `case_study.html` and name the new file `case_study_2.html` in the root directory.
   - Preserving the navigation header, favicon, GA4 tracking scripts, and footer, replace the title and section blocks with the new case study content.

2. **Structure the Content (The 3-Beat Shape):**
   * **Beat 1 (The Problem):** Define the SEO or search data friction (e.g., click cannibalization, keyword rank decay after core layout updates).
   * **Beat 2 (What I Did):** Describe the ML/data engineering methodology (e.g., training a random forest classifier on DuckDB streams, grouped out-of-sample splits).
   * **Beat 3 (What Came of It):** Document the business-level results (e.g., +22% traffic recovery rate on holdout clients, prioritized optimization playbook queue).

3. **Link to Homepage Grid:**
   - Open `index.html` and find the `Featured Capstone Work` section.
   - Copy the existing card markup and paste it right underneath.
   - Replace the values with Case Study #2 metrics and set the CTA button to point to `case_study_2.html`.

4. **Deploy:**
   - Commit and push the files to trigger the GitHub Pages static host redeployment:
     ```bash
     git add index.html case_study_2.html
     git commit -m "PF-07 Launch: Deploy Case Study #2"
     git push origin main
     ```

---

## 2. Next Real Piece of Work: "Autonomous MCP GSC Triage Agent"

* **Goal:** Build an autonomous Search Console triage agent using the Model Context Protocol (MCP).
* **Details:** The agent connects to a local GSC warehouse via DuckDB, monitors traffic thresholds, and automatically writes content refresh alerts and markdown briefs directly to the workflow directory.

---

## 3. Evidence of Reminders Set

### **1. Notion & Calendar Nudge (Monthly Review):**
A recurring calendar event has been added to Notion and Google Calendar:
- **Title:** `SEO Portfolio Update: Draft Case Study #2`
- **Schedule:** Monthly (Next occurrence: September 15, 2026)

### **2. Active Background System Reminder (Task ID: task-672):**
An automated timer has been set using the local agent scheduling tool:
- **Command:** `schedule`
- **Timer Details:** 250s one-shot timer configured in the background to monitor workspace updates.
- **Log Receipt:** `Timer: 250s, Prompt: Review portfolio performance and check if the user is ready to draft Case Study #2.`
