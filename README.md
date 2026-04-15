# Playwright Automation Test Suite

## Project description
A Python-based web UI automation project built with Playwright and pytest. The suite uses a page object model to encapsulate page actions and includes a smoke test that exercises application login behavior.

## Tech stack
- Python
- pytest
- Playwright
- pytest-playwright
- Page Object Model pattern

## Project structure
- `conftest.py` — pytest fixture configuration and browser setup
- `Pages/`
  - `a_login_page.py` — login page actions
  - `add_patient_page.py` — patient creation actions
  - `patient_records.py` — patient record-related actions
- `Tests/`
  - `smoke_test.py` — smoke-level end-to-end test
- `.venv/` — local virtual environment (excluded from source control)
- `.pytest_cache/` — pytest cache directory (excluded from source control)

## Installation

1. Create and activate a virtual environment

   Windows PowerShell:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   Windows CMD:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

2. Install dependencies

   If a `requirements.txt` file is available:
   ```bash
   pip install -r requirements.txt
   ```

   Otherwise:
   ```bash
   pip install pytest playwright pytest-playwright
   python -m playwright install
   ```

## Running tests

- Run the full test suite:
  ```bash
  pytest
  ```

- Run the smoke test:
  ```bash
  pytest Tests/smoke_test.py
  ```

- Run a specific test or subset by keyword:
  ```bash
  pytest Tests/smoke_test.py -k smoke
  ```

- Run with concise output:
  ```bash
  pytest -q
  ```

## Environment setup
- Ensure Python 3.10+ is installed
- Activate the project virtual environment before running tests
- Install Playwright browser dependencies with:
  ```bash
  python -m playwright install
  ```

## Reporting
- No dedicated reporting tool configuration (Allure or similar) was detected in this repository.
- If Allure reporting is added later:
  ```bash
  pip install allure-pytest
  pytest --alluredir=allure-results
  allure serve allure-results
  ```

## CI/CD
- No CI/CD pipeline configuration was detected in the current repository.
- Recommended CI/CD flow:
  1. install Python environment
  2. install package dependencies
  3. install Playwright browsers
  4. run `pytest`
  5. publish any generated test report artifacts

## Notes
- The project follows a page object design for better maintainability.
- Keep credentials and other secrets out of source control.
