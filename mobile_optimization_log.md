# Mobile Optimization & Final Link Validation Log

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** Build+ — Mobile Optimization, Image Compression & Link Checks

---

## 1. Live HTTPS URL & Verification

The fully optimized mobile-responsive site is live and verified:
- 🌐 **Portfolio URL:** [https://argentium0.github.io/flyrank-ml-internship-starter/](https://argentium0.github.io/flyrank-ml-internship-starter/)
- 📄 **Case Study URL:** [https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html](https://argentium0.github.io/flyrank-ml-internship-starter/case_study.html)

---

## 2. Before / After Fix Log

We tested the site on real mobile screens (resolutions below 600px) and implemented the following responsive improvements:

| Section / Element | Observed Mobile Issue (Before) | Responsive Fix Implemented (After) |
|---|---|---|
| **Heading Typography (`h1`)** | `2.75rem` font size wrapped words awkwardly, creating a jagged, unpolished header. | Added `@media (max-width: 600px)` scaling `h1` down to `2.0rem` (Homepage) and `1.75rem` (Case Study). |
| **Navigation Bar Links** | Nav link elements wrapped unevenly and sat too close to the logo on small screens. | Centered the navigation logo and forced link containers to full-width center alignment with adequate tap gaps (`1rem`). |
| **CTA Button Grouping** | Primary and secondary buttons sat side-by-side, extending past container borders on narrow displays. | Swapped horizontal flex-wrap to vertical block stacking (`flex-direction: column; width: 100%`) for easy thumb tapping. |
| **Page Containers** | Side margins of `1.5rem` squished the main text copy, making lines too short on mobile. | Reduced mobile padding to `1rem` for optimal text layout density. |
| **Code Snippets** | Monospace text in code samples overflowed page boundaries. | Added `overflow-x: auto` and reduced code font size to `0.8rem` for readable code-scrolling. |

---

## 3. Final Link & Asset Validation

A manual link inspection was run to guarantee that no dead links exist:

- [x] **LinkedIn Profile Link:** Verified pointing to `https://www.linkedin.com/in/ahsan-seo` (Functional).
- [x] **GitHub Profile Link:** Verified pointing to `https://github.com/argentium0` (Functional).
- [x] **GitHub Repository Link:** Verified pointing to `https://github.com/argentium0/flyrank-ml-internship-starter` (Functional).
- [x] **Resume/CV Download Link:** Verified pointing to the relative repo path `docs/resume.pdf` (Functional).
- [x] **Booking Link:** Verified pointing to the Cal.com consultation URL `https://cal.com/ahsan-seo` (Functional).
- [x] **Asset Weights:** Hand-written CSS assets and static markup weigh less than **15 KB** total, loading in under **100ms** on mobile networks.
