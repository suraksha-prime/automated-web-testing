# Automated Web Testing & Reporting

## Project Overview
A beginner-friendly web automation project using Python and Playwright to test important user workflows on a demo e-commerce website. Test results are stored in PostgreSQL, with n8n used to demonstrate test-result processing and reporting.

## Technologies Used
- Python
- Playwright
- PostgreSQL
- SQL
- n8n

## Automated Test Cases
- Verify successful login.
- Verify invalid login.
- Verify adding a product to the cart.
- Verify removing a product from the cart.

## Database
Test execution results are stored in a PostgreSQL table named `test_results`.

## How to Run
1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Configure database credentials in a local `.env` file.
5. Run the tests from the project root.

Example:

```bash
python -m tests.test_login
python -m tests.test_invalid_login
python -m tests.test_add_to_cart
python -m tests.test_remove_from_cart
```

## Note
This project is for learning and demonstration purposes. The browser tests run against a demo website.
