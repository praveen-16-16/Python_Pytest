import pytest
from arithmetics import div

def test_div(input_values):
    a, b = input_values

    if b == 0:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            div(a, b)
        return  # Skip assertion if division by zero

    result = div(a, b)
    expected = a / b
    print(f"\nDivision ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
