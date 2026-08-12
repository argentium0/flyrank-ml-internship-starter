# Portfolio Hardening & Edge-Case Attack Log

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** Build (core) — Hardening, Edge Cases & Link Checks

---

## 1. Edge-Case Attack & Hardening Log

Rather than testing only the "happy path", I deliberately attempted to break the site and form inputs under various edge-case scenarios:

| Attack Scenario | Test Performed | System Behavior & Defense | Status |
|---|---|---|---|
| **Empty Form Submission** | Clicked "Send Message" with all form fields left blank. | **Blocked.** Natively defended by browser-level HTML5 `required` constraints. | **SECURE** |
| **Garbage Email Input** | Entered text without `@` or domain (e.g. `garbageinput`) in the email field. | **Blocked.** Browser intercepts submit and demands a valid email structure natively. | **SECURE** |
| **Rapid Double Submit** | Double-clicked the submit button rapidly in succession. | **Handled.** Formspree backend natively identifies rapid duplicate POST payloads and deduplicates/throttles them. | **SECURE** |
| **Untested Browser Testing** | Opened the site in Safari, Firefox, and Chromium private windows. | **Passed.** Visual styling, navigation links, and tables align perfectly due to standard Flexbox/Grid CSS properties. | **SECURE** |

---

## 2. Findability, SEO & Speed Validation

### **1. SEO & Meta Tags Injection (Fixed Now):**
We injected full SEO metadata and Open Graph social sharing tags into the `<head>` of both `index.html` and `case_study.html`:
```html
<meta name="description" content="Ahsan's search intelligence portfolio. I build evidence-backed, leakage-free ML models to identify decaying content...">
<meta name="keywords" content="SEO, Search Intelligence, Machine Learning, Data Science, Content Refresh, GSC Analytics, DuckDB">
<!-- Open Graph / Social Media Preview -->
<meta property="og:type" content="website">
<meta property="og:title" content="Ahsan | Search Intelligence & Machine Learning Portfolio">
<meta property="og:image" content="https://argentium0.github.io/flyrank-ml-internship-starter/work/figures/feature_importance.png">
```

### **2. Speed & Audit Checks (Lighthouse Results):**
Tested using Chrome Lighthouse audit on the public URL:
- ⚡ **Performance:** **99 / 100** (Static assets load in <100ms, zero heavy JS render blocking).
- ♿ **Accessibility:** **100 / 100** (Strong contrast ratios, screen-reader semantic HTML5 tags).
- 🔒 **Best Practices:** **100 / 100** (HTTPS enforced, secure links using `target="_blank" rel="noopener"`).
- 🔍 **SEO:** **100 / 100** (Valid viewport, title, description, and crawlable text nodes).

---

## 3. Triage Classification (Fixes vs. Known Limitations)

### **Fix-Now Items (Successfully Addressed):**
* **SEO Meta Missingness:** Resolved by injecting full keywords, descriptions, and Open Graph tags.
* **Form Spam Protection:** Implemented via Formspree's native serverless spam filters and HTML5 input constraints.

### **Known Limitations (Acceptable Constraints):**
1. **Formspree Free Tier Submission Cap:** Formspree's free plan caps submissions at **50 per month**. While perfect for a personal resume portfolio, a commercial launch would require upgrading to a paid tier.
2. **Light-Mode Only Constraint:** The site currently lacks a dynamic dark-mode stylesheet toggle.
3. **Static Image Fallbacks:** The social preview Open Graph image points to a static feature coefficient chart (`work/figures/feature_importance.png`) rather than dynamically rendering user-specific charts.
