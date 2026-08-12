# Portfolio Critique & Design Review Report (Survive the Crit)

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** PF-07 — Design Review & Portfolio Critique

---

## 1. Submitted Proof Statement

The live portfolio was submitted to a peer/technical reviewer alongside our official proof statement:

> **Proof Statement:**  
> *"I build evidence-backed, leakage-free ML models that identify declining search content and prioritize optimization opportunities across millions of rows of Google Search Console data."*

---

## 2. Reviewer Feedback & The 10-Second Test

The reviewer evaluated the live site at [https://argentium0.github.io/flyrank-ml-internship-starter/](https://argentium0.github.io/flyrank-ml-internship-starter/) and answered the two mandatory critique questions:

### **Question 1: In 10 seconds, what do I do?**
- **Reviewer Response:**  
  *"You build machine learning models for search engine optimization (SEO) that scan millions of rows of search console data to find decaying content pages."*
- **Assessment:** **Passed.** The positioning statement and hero typography immediately communicated the core track specialization.

### **Question 2: Would you believe I'm good at it?**
- **Reviewer Response:**  
  *"Yes. The +36% precision metric box right below the headline and the explicit Leakage Trap experiment box in the case study make your claims feel backed by real data rather than marketing fluff."*
- **Assessment:** **Passed.** The quantitative proof elements landed as intended.

---

## 3. Honest Feedback Categorization

Rather than defending the original design, all reviewer feedback was collected and categorized into **Must-Fix** (critical clarity/usability issues) and **Nice-to-Have** (future polish):

```
                       Reviewer Feedback Stream
                                  |
         +------------------------+------------------------+
         |                                                 |
[ Must-Fix Items (Addressed Now) ]         [ Nice-to-Have Items (Future) ]
  1. Low CTA Button Hierarchy Contrast       1. Interactive Table Filtering
  2. Mobile Table Cell Squishing             2. Dark Mode Toggle Switch
  3. Missing Active Nav Link Indicator       3. Micro-Animation Hover States
```

### **Must-Fix Items (Addressed Immediately):**
1. **CTA Button Hierarchy Contrast:** The primary CTA button (`Read Capstone Case Study`) used dark border styling identical to secondary outline buttons, diluting the main visual path.
2. **Mobile Table Responsiveness:** Evaluation tables on mobile screens squished text columns vertically, making the model comparison hard to read on smartphones.
3. **Active Nav Link Highlight:** The navigation menu lacked an active indicator showing which page was currently open (`Home` vs `Case Study`).

### **Nice-to-Have Items (Deferred to Future Polish):**
1. Adding interactive column filtering or search bars for the candidate recommendation table.
2. Adding a dark mode theme toggle switch.
3. Adding subtle animated hover states for skills grid cards.

---

## 4. Evidence of Addressed Must-Fixes on Live Site

All three **Must-Fix** items were addressed directly in code, committed, and pushed live:

- **Fix 1 (CTA Contrast):** Re-styled `.btn-primary` with a solid vibrant brand blue (`#2563EB`) background and subtle drop shadow (`box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2)`), creating an unmistakable visual hierarchy.
- **Fix 2 (Mobile Tables):** Added `min-width: 500px` and a rounded border container (`.table-responsive`) around all tables, guaranteeing smooth horizontal scrolling without text squishing on mobile devices.
- **Fix 3 (Active Nav Indicator):** Added active link border styling (`border-bottom: 2px solid var(--brand-color); font-weight: 600`) to clearly highlight the active page.

### **Live Verification Links:**
- 🌐 **Updated Homepage:** [https://argentium0.github.io/flyrank-ml-internship-starter/](https://argentium0.github.io/flyrank-ml-internship-starter/)
- 📄 **Updated Case Study:** [https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html](https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html)
