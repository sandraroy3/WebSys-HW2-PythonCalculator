# IS601 Web Systems Development Homework 2


This assignment involves setting up a professional Python development environment with virtual environments, automated testing, static analysis, and version control. Here’s a step-by-step guide to help you complete it successfully.

**Step 1: Install Python and Virtual Environment Manager**

Here I am using Ubuntu, so install pipun:

`sudo apt update -y` <br> 
`sudo apt install python3-pip` <br>
`pip3 --version  # Verify installation` <br>

Install the virtual environment manager globally:<br>
`pip3 install virtualenv`

**Step 2: Clone the Instructor's Project (Test Setup)**

To ensure everything works, first clone the instructor’s repo:<br>
`git clone git@github.com:kaw393939/git_python_testing_setup_homework.git
cd git_python_testing_setup_homework
source venv/bin/activate  # Activate the virtual environment, If it errors, create a venv folder.
pip3 install -r requirements.txt  # Install dependencies
pytest --pylint --cov  # Run tests, linting, and coverage`

**Step 3: Create my Own Project**

Navigate out of the instructor’s project and create your own project directory:

`cd ..`<br>
`mkdir myPythonProj`<br>
`cd myPythonProj`<br>

Create and Activate a Virtual Environment

`virtualenv venv`<br>
`source venv/bin/activate`

The terminal should now show (venv) indicating that the virtual environment is active.

This assignment involves setting up a professional Python development environment with virtual environments, automated testing, static analysis, and version control. Here’s a step-by-step guide to help you complete it successfully.

**Step 4: Install Dependencies**

Inside your virtual environment, install required Python packages:<br>
`pip3 install pytest pytest-pylint pytest-cov`

Freeze Dependencies<br>
Save dependencies to a requirements.txt file:<br>
`pip3 freeze > requirements.txt`<br>
Now, anyone cloning your project can install dependencies using: <br>
`pip3 install -r requirements.txt`

**Step 5: Set Up Project Structure**

Inside myPythonProj/, create the necessary folders and files:

`mkdir -p calculator tests`<br>
`touch calculator/__init__.py tests/__init__.py .gitignore .pylintrc pytest.ini`<br>
Copy the contents of .gitignore, .pylintrc, and pytest.ini from the instructor’s project.

**Step 6: Write Code and Tests**

Create calculator/__init__.py with the following simple function:<br>
```python
def add(a: int, b: int) -> int:
    return a + b
```

Add remaining calculator functions as needed.


Create tests/test_calculator.py:
```python
from calculator import add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0 
```

Add remaining calculator functions as needed.


**Step 7: Run Tests, Linting, and Coverage**

Run basic tests:<br>
`pytest`

Run tests with pylint static analysis:<br>
`pytest --pylint`

Run tests with coverage:<br>
`pytest --pylint --cov`

**Step 8: Use Git for Version Control**

Initialize a Git repository:

`git init`<br>
`git add .`<br>
`git commit -m "Initial project setup"`<br>
`git branch -M main`<br>
`git remote add origin <your-repo-url>`<br>
`git push -u origin main`<br>
