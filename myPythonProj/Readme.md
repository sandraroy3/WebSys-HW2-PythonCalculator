# Project: Preparing for Production – DevOps, Cloud Computing, Logging, and CI/CD
This project integrates GitHub Actions, environment variables, and logging to prepare a Python application for a production environment.

## Features
1. GitHub Actions (CI/CD) – Runs tests automatically when pushing to main.
2. Environment Variables – Securely stores sensitive information.
3. Logging – Implements structured logging instead of print() for better debugging.

## Setup Instructions
1️⃣ Clone the Repository  
git clone https://github.com/your-username/your-repo.git  
cd your-repo  
2️⃣ Create a Virtual Environment  
python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
3️⃣ Install Dependencies  
pip install -r requirements.txt  

## Environment Variables Setup  
Create a .env file in the project root:  
``ENVIRONMENT=development
API_KEY=your_secret_api_key
``
Ensure .env is ignored by adding this to .gitignore:

## Logging Implementation
The project uses the Python logging module:


import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Application started")

### Continuous Integration (CI) with GitHub Actions
1️⃣ Workflow Setup
The GitHub Actions workflow is in .github/workflows/python-app.yml and runs tests on push to main.

2️⃣ Running Tests Locally
Run pytest to verify functionality:
pytest

📜 GitHub Actions Workflow Example
This workflow automatically runs tests:

name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: pytest
