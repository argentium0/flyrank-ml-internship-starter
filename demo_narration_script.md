# Capstone Agent Demo: Narration Script & Screen Outline

**Agent:** SearchScout-AI (Search Performance Decay Auditor)  
**Track:** Applied Search Intelligence Capstone  
**Target Video Duration:** 3 to 5 Minutes

---

## Screen Outline & Segment Breakdown

### **Segment 1: System Overview & JTBD (0:00 - 0:45)**
* **What to Show:** Open [agent_readme.md](file:///c:/Users/Global%20Computers/Desktop/Ahsan/agent_readme.md) on your screen, highlighting the System Architecture flowchart.
* **Talking Points (Narration):**
  > *"Hi everyone, I'm Ahsan, and today I'm demonstrating **SearchScout-AI**, an autonomous Search Performance Decay Auditor built for SEO Managers and search analysts. 
  > 
  > Managing large content portfolios is highly resource-intensive. Editorial teams waste budget refreshing pages that have zero recovery potential. SearchScout-AI solves this by automating the audit loop. It queries our search performance warehouse, validates data contracts, scores decay risk, and formats strategic refresh briefs."*

---

### **Segment 2: Design Decision - Grouped Client Splits & Leakage Checks (0:45 - 1:45)**
* **What to Show:** Open [agent_mvp.py](file:///c:/Users/Global%20Computers/Desktop/Ahsan/agent_mvp.py) in your IDE. Scroll to `enforce_data_contract()`.
* **Talking Points (Narration):**
  > *"Let's talk about a key design decision: **how we validate our models**. 
  > 
  > A major trap in search performance modeling is client-identity memorization. If we split our data randomly, the model simply memorizes that 'Client A' gets huge traffic, masking its actual performance. We implemented a **Grouped Client Split** by client ID. This guarantees that our model is tested only on complete domains it has never seen before, proving it can generalize to new sites.
  > 
  > Additionally, to protect our data contract, we built this `enforce_data_contract` guardrail. If any post-decision features overlap the observation window, the agent immediately halts to prevent feature leakage."*

---

### **Segment 3: Live End-to-End Execution (1:45 - 3:00)**
* **What to Show:** Open a terminal window inside the workspace. Execute:
  `python agent_mvp.py`
* **Talking Points (Narration):**
  > *"Now let's watch the agent run end-to-end. I'll execute the script in our terminal. 
  > 
  > First, the agent initiates the DuckDB SQL connection and loads our 30,000-row content performance dataset into memory. 
  > Next, it queries candidate `content_17c2778a02a9`. 
  > Watch the logs: our zero-leakage contract check runs instantly and prints a pass receipt. 
  > The agent then calculates the decay score—assigning a score of 100.0/100, prioritizing the action label as `REFRESH_IMMEDIATELY`, and assigning reason code `stale_mid_volume_low_ctr`.
  > Finally, it outputs this clean, structured Markdown Search Intelligence Brief detailing the observed metrics, a strategic action plan, and an adversarial critique."*

---

### **Segment 4: Output Inspection & Language Guardrails (3:00 - 4:00)**
* **What to Show:** Scroll through the generated Markdown brief in the terminal. Highlight the `Adversarial Critique` and `Strategic Action Plan` sections.
* **Talking Points (Narration):**
  > *"Let's inspect the generated brief. The agent has outlined three on-page strategic tasks for our editorial team. 
  > 
  > But look at the next section: **the Adversarial Critique**. This is a core guardrail. The agent identifies why its own recommendation could be wrong—such as the page ranking too deep for content alone to recover, or a shift in search engine layouts suppressing organic clicks.
  > 
  > To ensure professional compliance, our agent also scans its output for forbidden causal language. If it detects unproven promises like 'will double your traffic' or 'guarantees rank #1', it blocks the output. As you can see, our brief successfully passes the check by using purely observational, decision-support wording like 'observed' and 'indicates'."*

---

### **Segment 5: Limitations & Closing (4:00 - 4:30)**
* **What to Show:** Open the **Known Limitations** section of [agent_readme.md](file:///c:/Users/Global%20Computers/Desktop/Ahsan/agent_readme.md).
* **Talking Points (Narration):**
  > *"To wrap up, here are the known limitations of the current build. First, SearchScout-AI cannot distinguish brand queries from informational search intent; brand homepages may return high prioritization scores but must be filtered manually. Second, the agent is restricted from making direct write operations to live websites or CMS databases.
  > 
  > The code and setup instructions are fully detailed in our repository. Thank you for watching!"*
