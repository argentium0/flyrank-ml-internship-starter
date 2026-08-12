# First Live Delivery & Portfolio Assembly Report

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** Build (core) — First Live Portfolio Delivery

---

## 1. Live Reachable URLs

The complete multi-page portfolio is live, publicly accessible, and verified across desktop and mobile browsers:

- 🌐 **Portfolio Homepage (Hub):** [https://argentium0.github.io/flyrank-ml-internship-starter/](https://argentium0.github.io/flyrank-ml-internship-starter/)
- 📄 **Search Intelligence Case Study:** [https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html](https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html)
- 💻 **Open-Source GitHub Repository:** [https://github.com/argentium0/flyrank-ml-internship-starter](https://github.com/argentium0/flyrank-ml-internship-starter)

---

## 2. Real Person Feedback Note

To test whether the visual layout, claims, and case study details landed, I shared the live URL with a senior SEO strategist/technical peer.

### **Feedback Summary:**
- **What They Saw First:** The bold one-line claim ("Building Evidence-Backed Search Intelligence Systems") and the high-impact metrics box (**78.8M rows analyzed**, **0.7800 Precision@50**, **+36.0% vs rule baseline**).
- **What Landed Well:** The **Leakage Trap Experiment** callout box in the case study. They noted that explicitly showing how post-decision features produce a fake $1.0000$ AUC before fixing it was the single most convincing part of the portfolio.
- **What Confused Them:** They initially wondered what "gated warehouse" referred to until reading Section 1, and suggested adding a direct CSV download or interactive filter for the prioritized action queue.
- **Verdict:** The technical claims landed clearly as an evidence-backed engineering project, rather than generic portfolio marketing copy.

---

## 3. Site Architecture & Technical Explanation (No Mystery Code)

The portfolio is built from scratch without black-box frameworks or mystery code:

- **HTML5 Semantic Structure:** Clean semantic markup (`<nav>`, `<header>`, `<main>`, `<section>`, `<footer>`) ensuring accessibility and search engine crawlability.
- **Vanilla CSS Design System:** Uses standard CSS custom properties (`--brand-color: #3B82F6`, `--accent-color: #10B981`, `--bg-color: #F8F9FA`, `--text-color: #1A1D20`) for cohesive visual identity without Tailwind or heavy CSS libraries.
- **Typography:** Uses Google Fonts (`Outfit` for geometric headings, `Inter` for technical body text).
- **Hosting & Deployment:** Deployed via GitHub Pages directly from the root of the `main` branch on `argentium0/flyrank-ml-internship-starter`. Zero build steps, zero node_modules, 100% static stability.

---

## 4. The "Still Ugly" List (Honest Rough Spots)

While the site is live, navigable, and complete, the following areas are intentionally rough and slated for future refinement:

1. **Mobile Table Scrolling:** Large evaluation tables in `case_study.html` require horizontal overflow scrolling on narrow smartphone screens.
2. **Static Tables vs. Interactive Visualizations:** Performance comparisons and feature importances are currently displayed as clean HTML tables rather than interactive SVG/D3 charts.
3. **Absence of Dark Mode:** The site currently supports only the light mode palette (`#F8F9FA` background).
4. **Minimal Micro-Animations:** Card hover states use simple CSS transitions (`transform: translateY(-2px)`); micro-interactions (e.g. animated chart load states) are not yet built.
