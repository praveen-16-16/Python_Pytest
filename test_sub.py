import pytest
from arithmetics import sub

def test_sub(input_values):
    a, b = input_values
    result = sub(a, b)
    expected = a - b
    print(f"\nSubtraction ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
