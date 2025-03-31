import pytest
from arithmetics import add

def test_add(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    result = add(a, b)
    expected = a + b
    print(f"\nAddition ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
