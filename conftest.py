import pytest

def pytest_addoption(parser):
    parser.addoption("--a", action="store", type=int, help="First number")
    parser.addoption("--b", action="store", type=int, help="Second number")

@pytest.fixture
def input_values(request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")

    if a is None or b is None:
        pytest.skip("Skipping test: Missing command-line arguments.")

    return a, b
