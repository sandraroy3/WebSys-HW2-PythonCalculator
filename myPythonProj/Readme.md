# Python Interactive Calculator with Commands, Plugins & Multiprocessing

## Overview
This project is a **command-line interactive calculator** that follows the **Command Pattern** and **Plugin Architecture**. The application dynamically loads commands (plugins) and executes them **using multiprocessing** to enhance performance. 

Supported **calculator operations**:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`) *(with division by zero handling)*
- Menu (`menu`) *(displays all available commands)*

**Key Features:**
- Modular **plugin-based** architecture.
- **Multiprocessing** for command execution.
- **Dynamic command loading** (new plugins auto-register).
- **Robust error handling** (division by zero, invalid inputs).

---

## Overview
This project is a **command-line interactive calculator** that follows the **Command Pattern** and **Plugin Architecture**. The application dynamically loads commands (plugins) and executes them **using multiprocessing** to enhance performance. 

Supported **calculator operations**:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`) *(with division by zero handling)*
- Menu (`menu`) *(displays all available commands)*

**Key Features:**
- Modular **plugin-based** architecture.
- **Multiprocessing** for command execution.
- **Dynamic command loading** (new plugins auto-register).
- **Robust error handling** (division by zero, invalid inputs).

---

##  **How to Run**
### **1️⃣ Install Dependencies**
Before running, ensure you have Python installed. Then, install required dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt #pip install required packages
python main.py # Run the Application
```

## Using the Menu
To see all available commands, type:  
```
Enter command: menu
Available commands: add, subtract, multiply, divide, menu

4️⃣ Execute Commands
Enter command: add  
Enter first number: 5  
Enter second number: 3  
Process Process-1: Result = 8.0  

Enter command: divide  
Enter first number: 10  
Enter second number: 2  
Process Process-2: Result = 5.0  
```

## Understanding Plugins
The commands are stored inside the plugins/ directory, making it easy to add new commands dynamically.
When the program starts, it automatically loads all plugins without modifying main.py.
Each plugin implements its own logic and registers itself via a register() function.

## Multiprocessing
Each command runs in a separate process using multiprocessing.
This prevents blocking the REPL loop, making the calculator more responsive.
The process name is displayed in the output:

# Running Tests
1️⃣ Run All Tests<br>
pytest --cov=app

2️⃣ Test Plugin Commands <br>
pytest tests/test_plugins.py

3️⃣ Test Multiprocessing<br>
pytest tests/test_multiprocessing.py