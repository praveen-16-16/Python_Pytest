
import pytest
from arithmetics import sub

def test_sub(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    result = sub(a, b)
    expected = a - b
    print(f"\nSub ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
