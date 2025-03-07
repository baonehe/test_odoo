# test_odoo
# Running Tests for Employee Skills Module

This document explains how to run automated tests for the `employee.skills` module in Odoo using Pytest.

## Prerequisites
Before running the tests, ensure you have:
- A working Odoo development environment.
- The `pytest` package installed.

To install pytest, run:
```bash
pip install pytest
```

## Setting Up the Test Environment
1. Navigate to your Odoo instance directory.
2. Ensure your custom module `employee.skills` is installed and available in Odoo.
3. Create a `tests/` folder inside the module if it doesn't already exist.
4. Ensure your test files are inside `tests/` (e.g., `test_employee_skills.py`).

## Running the Tests
To execute all test cases, use the following command inside your Odoo instance:
```bash
pytest --maxfail=1 --disable-warnings -q
```

### Running a Specific Test File
To run a specific test file, use:
```bash
pytest tests/test_employee_skills.py
```

### Running a Specific Test Case
To run a single test case, use:
```bash
pytest -k "test_email_sent_for_critical_skill"
```

### Running Tests with Detailed Output
For more detailed output, use:
```bash
pytest -v
```

## Understanding the Test Structure
- **Fixtures**: Used to create test data before each test case runs (e.g., creating employee records).
- **Mocking**: `patch` is used to simulate email sending without actually sending emails.
- **TransactionCase**: Odoo rolls back database changes after each test to ensure a clean state.

## Debugging Failures
If a test fails, rerun it with detailed output:
```bash
pytest -v --tb=short
```

If needed, enable debugging by adding `--pdb`:
```bash
pytest --pdb
```

## Additional Notes
- Always restart your Odoo instance before running tests if you have modified models.
- Ensure no other processes are interfering with the test database.

Using AI to Optimize Best Practices

Prompts Used

To research best practices for writing tests in Odoo with Pytest, I used AI (ChatGPT) with prompts such as:

"How to write Pytest test cases for an Odoo module?"

"Best practices for using Pytest fixtures in Odoo?"

"How to mock email sending in Odoo tests using Pytest?"

Validation of AI Suggestions

To ensure the AI-generated code and advice were correct:

I cross-checked with Odoo’s official documentation.

I tested sample code in a local Odoo environment.

I referred to existing Odoo community best practices and GitHub repositories.