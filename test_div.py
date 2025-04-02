import pytest
from arithmetics import div

def test_div(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    result = div(a, b)
    expected = a + b
    print(f"\nDivition ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
