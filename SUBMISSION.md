# Submission Instructions and Artifacts

What I changed
- Updated `package.json` to add a `start` script: `npx http-server ./web -p 8000`.
- Added `cypress.config.js` to configure Cypress `baseUrl`.
- Updated Cypress spec: `automation/cypress/e2e/registration.spec.js`.
- Enhanced UI styles: `web/styles.css` (gradient background, shiny header effect, button styling).
- Updated Selenium script to save screenshots and a log: `automation/selenium/selenium_tests.py`.

Artifacts produced
- `screenshots/negative.png` — Selenium negative-case screenshot
- `screenshots/positive.png` — Selenium positive-case screenshot
- `screenshots/selenium_results.log` — Selenium run log
- `cypress/screenshots/registration.spec.js/error-state.png` — Cypress negative screenshot
- `cypress/screenshots/registration.spec.js/success-state.png` — Cypress positive screenshot

How to run locally

1. Start the static server from project root:
```powershell
cd C:\xampp\htdocs\registration-system
npm start
```

2. Run Cypress (headless):
```powershell
npx cypress run --spec "automation/cypress/e2e/registration.spec.js"
```

3. Run Selenium tests (requires ChromeDriver and the `selenium` Python package):
```powershell
python -m pip install selenium
python automation/selenium/selenium_tests.py
```

Where outputs are saved
- Selenium artifacts: `screenshots/`
- Cypress artifacts: `cypress/screenshots/registration.spec.js/`

Notes
- The Cypress negative test was adjusted to trigger validation programmatically so it runs reliably in headless CI.
- If you want, I can also add a `test:e2e` script to `package.json` to run Cypress via `npm run test:e2e`.
