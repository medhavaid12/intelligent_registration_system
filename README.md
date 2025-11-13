# Registration System — Project README

This project contains:
- `web/` — registration form (HTML/CSS/JS)
- `automation/cypress/` — Cypress end-to-end tests
- `automation/selenium/` — simple Selenium tests (Python)
- `screenshots/` — screenshots produced by automation
- `registration-system.zip` — (downloadable package)

---

## Quick preview (no install)
Open `web/index.html` in your browser:
- Double-click `web/index.html` OR
- Serve from a simple static server (recommended) and open `http://localhost:8000/web/index.html`.

---

## Recommended environment
- Node.js (v16 or newer) + npm
- Chrome browser (for Cypress / Selenium)
- Python 3.8+ (for Selenium script)
- Git (optional)

---

## Option A — Serve the site quickly (recommended)
Some browsers or test tools behave better when the site is served over HTTP rather than opened via `file://`. Use one of these:

### Using Python (quick)
```bash
# from project root
cd registration-system
# Python 3
python3 -m http.server 8000
# open http://localhost:8000/web/index.html
