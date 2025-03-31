import pytest

def pytest_addoption(parser):
    parser.addoption("--a", action="store", type=int, help="First number")
    parser.addoption("--b", action="store", type=int, help="Second number")
    parser.addoption("--c", action="store", type=int, help="Third number")
