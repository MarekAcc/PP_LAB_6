"""Simple calculator"""


def add(a: int, b: int) -> int:
    """Add function"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Substract function"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply function"""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide function"""
    return a / b


def binary_converter(a: int) -> str:
    """Binary converter"""
    if not isinstance(a, int) or a < 0:
        raise ValueError("Input must be a non-negative integer.")
    return bin(a)
