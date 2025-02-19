import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide 

fake = Faker()

def pytest_generate_tests(metafunc):
    # Check if the test function already has parameterization
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        
        metafunc.parametrize(
            ("a", "b", "operation", "expected"),
            [(a, b, op_name, expected) for a, b, op_name, op_func, expected in parameters]
        )


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

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "operation", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation,expected", parameters)
