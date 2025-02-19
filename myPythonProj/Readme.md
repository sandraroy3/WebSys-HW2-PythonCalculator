# **Python Calculator Project with Faker**

## Project Overview
This project implements a **Python-based calculator** using **Object-Oriented Programming (OOP)** principles. It supports **addition, subtraction, multiplication, and division** operations while maintaining a history of calculations.

The project includes:
- **OOP Principles**: Encapsulation, Inheritance, and Polymorphism
- **Unit Testing**: `pytest`
- **Test Coverage**: `pytest-cov`
- **Static Code Analysis**: `pylint`
- **CLI Support**: Interactive command-line interface
- **Faker Integration**: Generate random test data for validation

---

## **📂 Project Structure**
```bash
myPythonProj/
│── calculator/          # Calculator logic
│   ├── __init__.py
│   ├── operations.py    # Functions: add, subtract, multiply, divide
│   ├── calculation.py   # Single calculation class
│   ├── calculations.py  # Manages calculation history
│
│── tests/               # Unit tests
│   ├── __init__.py
│   ├── conftest.py      # Pytest fixtures
│   ├── test_calculator.py  # Unit tests for calculator functions
│   ├── test_main.py     # CLI tests
│
│── main.py              # CLI implementation
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
│── pytest.ini           # Pytest configuration
│── .pylintrc            # Pylint configuration
```

## Installation and Setup
Step 1: Create a Virtual Environment
```python
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

Step 2: Install Faker and freeze to requirements.txt
```python
pip install faker
pip freeze > requirements.txt
```

Step 3: Generating Fake Test Data
Faker is used to generate random numbers for test cases, ensuring robustness.

Example usage in conftest.py:
```python
def generate_test_data(num_records):
    """Generate random test cases for the calculator."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_int(min=1, max=100))
        b = Decimal(fake.random_int(min=1, max=100))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide and b == 0:
            expected = "ZeroDivisionError"
        else:
            expected = operation_func(a, b)

        yield a, b, operation_name, expected
```

Step 4: Testing

Test data functionality <br>
`pytest --num_records=10`

Test coverage <br>
`pytest --cov=calculator --cov-report=term-missing`

Test user input functionality on the command line: <br>
`python main.py 1 2 add` <br>
Getting output as below:
The result of 1 add 2 is equal to 3