# gcd.py

def gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)
