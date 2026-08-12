# Portfolio Tech Stack Rationale

This document outlines the comparative analysis and decision rationale for selecting the portfolio website's technical stack.

## 1. The Constraints

- **Free Only:** The hosting, deployment, and assets must incur \$0 operational costs.
- **Skill Level:** Solid familiarity with Python, Git, Markdown, and basic HTML/CSS. No deep experience with complex JavaScript state-management or dynamic frameworks.
- **Portfolio Needs:** A clean, multi-page layout (Homepage + Case Study Details) to present technical analysis. No dynamic backend databases are required yet (all analytics results are pre-computed static summaries).
- **Display Requirements:** High-resolution cropped screenshots, clean visual charts (PNG/SVG), embedded links to Colab notebooks, and code links to the GitHub repository.

---

## 2. Three Roads Analyzed

### **Road 1: Pure HTML / Vanilla CSS on GitHub Pages (Simplest)**
- **How to Build:** Write plain HTML5 pages and a single, custom CSS stylesheet using variables to implement the identity kit.
- **Where to Host:** GitHub Pages (free).
- **Backend Needed:** None.
- **The Trade-off:** Extremely fast load times and zero build dependencies. The primary trade-off is the lack of layout templating, meaning the header and footer HTML must be repeated on each page.

### **Road 2: Hugo / Eleventy Static Site Generator (Mid-Tier)**
- **How to Build:** Write layouts in HTML templates and content in Markdown files, compiled locally into static assets.
- **Where to Host:** Netlify or GitHub Pages (free).
- **Backend Needed:** None.
- **The Trade-off:** Clean file separation and layout inheritance. The trade-off is a minor learning curve to learn the templating engine (e.g., Go templates or liquid) and configuring build pipelines.

### **Road 3: Next.js (React) on Vercel (Most Powerful)**
- **How to Build:** Modular component architecture using React components.
- **Where to Host:** Vercel (free).
- **Backend Needed:** Not needed (but supported via Serverless Functions).
- **The Trade-off:** Extremely robust component modularity and smooth page transitions. The trade-off is high overhead, package dependency maintenance (NPM updates), and slower build times for a simple static page.

---

## 3. Pressure-Testing & Rationale

**Why I Chose Road 1 (Pure HTML/CSS on GitHub Pages):**
- **Maintenance & Friction:** Pure HTML/CSS requires zero maintenance. There are no node modules to break, no version conflicts, and no build configurations to troubleshoot.
- **Visual Control:** Vanilla CSS variables allow strict adherence to the identity kit palette.
- **Time Constraint:** With a two-week timeline, I want to spend 95% of my time refining my data contract claims and signal reports, rather than debugging NPM packages or Next.js build errors.
- **Why I Rejected the Alternatives:**
  - *Hugo (Road 2)* was rejected because it introduces unnecessary templating syntax for a simple two-page site.
  - *Next.js (Road 3)* was rejected because it is heavy overkill. Managing React state or framework hydration is unnecessary for static markdown and charts.
