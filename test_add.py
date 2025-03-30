import pytest
from arithmetics import add

def test_add(input_values):
    a, b = input_values
    result = add(a, b)
    expected = a + b
    print(f"\nAddition ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
