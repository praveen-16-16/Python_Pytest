import pytest
from arithmetics import mul

def test_mul(input_values):
    a, b = input_values
    result = mul(a, b)
    expected = a * b
    print(f"\nMultiplication ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
