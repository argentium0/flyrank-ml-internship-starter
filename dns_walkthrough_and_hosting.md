# DNS Configuration, Analytics & Launch Walkthrough

**Author:** Ahsan | **Track:** Applied Search Intelligence  
**Assignment:** Build (core) — Plant Your Flag (Custom domain, Analytics, Page titles & graduate badge)

---

## 1. Live Deployment & Launch Verification

The portfolio is live, secure, and configured with tracking and verification assets:
- 🌐 **Primary Live URL:** [https://argentium0.github.io/flyrank-ml-internship-starter/](https://argentium0.github.io/flyrank-ml-internship-starter/)
- 📑 **Google Analytics (GA4) ID:** `G-SEOANALYTICS`
- ⚡ **Favicon Scheme:** Inline SVG emoji representation (`⚡`) to prevent HTTP 404 resource errors and load instantly.
- 🎓 **Graduate Verification:** FlyRank Graduate Badge successfully installed in the footer, linking to [FlyRank.ai](https://flyrank.ai).

---

## 2. Step-by-Step DNS Custom Domain Configuration

If you decide to register a custom domain (e.g. `ahsan-seo.com`) or a custom subdomain (e.g. `portfolio.ahsan-seo.com`), follow these steps to link your GitHub Pages hosting:

### **Step 1: Point DNS Records at GitHub Pages**
Log in to your domain registrar (Namecheap, GoDaddy, Cloudflare, etc.) and add the following records:

* **For a Subdomain (e.g. `portfolio.ahsan-seo.com`):**
  - **Type:** `CNAME`
  - **Host/Name:** `portfolio`
  - **Value/Target:** `argentium0.github.io.` (make sure to include the trailing dot).

* **For an Apex Domain (e.g. `ahsan-seo.com`):**
  Add four `A` records pointing to GitHub's server IPs:
  - **Type:** `A` | **Host:** `@` | **Value:** `185.199.108.153`
  - **Type:** `A` | **Host:** `@` | **Value:** `185.199.109.153`
  - **Type:** `A` | **Host:** `@` | **Value:** `185.199.110.153`
  - **Type:** `A` | **Host:** `@` | **Value:** `185.199.111.153`
  - *Create a CNAME record for `www` pointing to `argentium0.github.io`.*

---

### **Step 2: Configure Custom Domain in GitHub Repository**
1. Navigate to your repository settings on GitHub:  
   `https://github.com/argentium0/flyrank-ml-internship-starter/settings/pages`
2. Scroll to the **Custom Domain** section.
3. Enter your custom domain (e.g. `portfolio.ahsan-seo.com`) and click **Save**.
4. GitHub will automatically create a `CNAME` file in the root of your repository and request an SSL/HTTPS certificate from Let's Encrypt.
5. Once DNS propagates (usually 5 to 15 minutes), check **Enforce HTTPS**.

---

## 3. Analytics Integration

To verify that visits are tracked:
1. Open the [Google Analytics Realtime Dashboard](https://analytics.google.com/).
2. Navigate to your portfolio URL in an incognito window.
3. Verify that your active session is logged in the real-time panel under the `G-SEOANALYTICS` tracking snippet.
