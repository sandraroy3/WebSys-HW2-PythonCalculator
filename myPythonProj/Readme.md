# IS601 Web Systems Development Homework 3

# 🧮 Improved Python Calculator  

## 📌 Overview  
This project is a **high-precision calculator** built using Python’s `decimal.Decimal` module, ensuring **accuracy and reliability** in arithmetic operations. It follows **Object-Oriented Programming (OOP)** principles and software design best practices like **SOLID, DRY, GRASP, and Separation of Concerns**.  
**SOLID** Principles:
Single Responsibility: Each class has a specific role (Calculation, Calculator, Calculations).
Open/Closed: Supports extension without modifying existing code.
Liskov Substitution: No unnecessary subclassing, methods work interchangeably.
Interface Segregation & Dependency Inversion: Classes interact with clearly defined methods.
**DRY** (Don’t Repeat Yourself): Common logic is reused through functions and methods.
**GRASP** (General Responsibility Assignment Software Patterns): Follows proper class responsibilities and interactions.
**Separation of Concerns**: Different files handle calculations, history management, and testing separately.

For this homework. what you need to do is to try to make the most complete calculator that can add, subtract, multiply, divide and store a history of calulations. The purpose of this assignment is to introduce you understand the principles of object oriented programming, unit testing, and design principles such as SOLID, DRY, GRASP, and Seperation of concerns. Its important to understand how to properly organize your code using the professional "grammer" of programming and not just the syntax of if statements and loops.



## ✅ Features  

- ✔ **Basic Arithmetic Operations** – Addition, Subtraction, Multiplication, Division  
- ✔ **Avoids Floating-Point Precision Issues** – Uses `decimal.Decimal` instead of `float`  
- ✔ **Calculation History** – Stores all previous calculations  
- ✔ **Error Handling** – Prevents division by zero  
- ✔ **Object-Oriented Design** – Implements **Static, Class, and Instance Methods**  
- ✔ **100% Test Coverage** – Automated unit testing with `pytest`  
- ✔ **Code Quality Assurance** – Uses `pylint` for clean, maintainable code  

---

## 📁 Project Structure  
📦 calculator_project ├── 📂 calculator # Core calculator modules │ ├── calculator.py # Calculator class with basic operations │ ├── calculation.py # Calculation & history management ├── 📂 tests # Unit tests using pytest │ ├── test_calculator.py ├── .gitignore # Ignore unnecessary files ├── requirements.txt # Required dependencies ├── README.md # Project documentation

## 📥 Installation & Setup  

### 🔹 Step 1: Clone the Repository  
```bash
git clone https://github.com/sandraroy3/WebSys-HW2-PythonCalculator.git
cd myPythonProj
git checkout HW3-improved_calculator #create new branch for hw3
```

### 🔹 Step 2: Create a Virtual Environment
```python
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 🔹 Step 3: Install dependencies
```python
pip install -r requirements.txt
```

### 🔹 Step 4: Run Tests
```python
pytest --pylint --cov
```

## Usage
Import and Perform Operations
```python
from decimal import Decimal
from calculator import Calculator
# Basic Operations
print(Calculator.add(Decimal("0.1"), Decimal("0.2")))  # Output: 0.3
print(Calculator.subtract(Decimal("5"), Decimal("2"))) # Output: 3
print(Calculator.multiply(Decimal("3"), Decimal("4"))) # Output: 12
print(Calculator.divide(Decimal("8"), Decimal("2")))   # Output: 4
```

Handling Calculation History
```python
from calculation import Calculation, Calculations

# Create a new calculation
calc1 = Calculation("add", Decimal("2"), Decimal("3"))
Calculations.add_calculation(calc1)

# Retrieve last calculation
last_calc = Calculations.get_last_calculation()
print(last_calc)  # Output: "2 add 3 = 5"

# Clear history
Calculations.clear_history()
```

Exception Handling (Division by Zero)
```python
try:
    Calculator.divide(Decimal("5"), Decimal("0"))
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
```


## Testing & Code Quality
🔹 Run Unit Tests<br>
`pytest
`

🔹 Check Code Quality with pylint<br>
`pylint calculator tests`

🔹 Check Test Coverage<br>
`pytest --cov=calculator --import-mode=importlib
`