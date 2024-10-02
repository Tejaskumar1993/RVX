# qa-automation-scripts

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

## Overview

This project is an automated testing suite designed to ensure the quality and functionality of ontrack-send applications. Using Playwright for browser automation and Pytest for testing, this suite includes a variety of test cases that validate the application's behavior across different environments (staging, dev and prod, test). The project leverages continuous integration (CI) with GITLAB to automatically run tests on code changes, providing fast feedback and maintaining high standards of code quality.

## Getting Started

### Prerequisites

List the software and tools required to run the project:
                                                                                                                      |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|                                                               |
| `Python 3.x`        | You can check if Python is installed by running this in your terminal: `python3 --version`<br/>Python download - https://www.python.org/downloads/ |
| `PIP`               | Pip download - https://pip.pypa.io/en/stable/installation/                                                                                                                                                                                                               |

### Installation

Step-by-step guide to installing the project and its dependencies.

```bash
# Clone the repository
git clone git@gitlab.pgprint.com:ontrack-applications/ontrack-send/qa-automation-scripts.git

# Navigate to the project directory
cd qa-automation-scripts

# Create a virtual environment
python3 -m venv venv
source env/bin/activate  # On Windows, use `env\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt

# Configure Playwright
playwright install

# Install Playwright browsers
python3 -m pip install --force-reinstall playwright
```
---
## Running Tests

Instructions for running the tests.

```bash
# Run all tests
pytest

# Run a specific test file on headed mode
pytest -k test_login_page_elements --headed
```
---
## Project Structure

Explain the structure of the project and the purpose of each directory.

| Package name   | Description                                                                    |
|:---------------|:-------------------------------------------------------------------------------|                          |
| `data`         | Data files used in tests                                                       | |
| `output_files` | Generated output files from tests and processes                                |
| `pages`        | Page object models representing different web pages and their methods          |
| `tests`        | Test cases sorted per application                                              |
| `utilities`    | Utility functions and helpers used across the project                          |
---

## Contributing
Guidelines for contributing to the project.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch). 
6. Create a new Pull Request.