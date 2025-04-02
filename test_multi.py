import pytest
from arithmetics import mul

def test_multi(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    result = mul(a, b)
    expected = a * b
    print(f"\nMulti ({a}, {b}) = {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
