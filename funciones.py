# funciones.py
from typing import Union
import math

Number = Union[int, float]


"""Validar que x sea int."""
def _filter_int(x, name: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError(f"{name} debe ser un entero (int), no {type(x).__name__}")
    return x

"""Valida que x sea número real (int o float)."""
def _filter_real(x, name: str) -> Number:
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError(f"{name} debe ser numérico (int o float), no {type(x).__name__}")
    return x


"""Resultado: cuadrado de un número real."""
def square(n: Number) -> Number:
    n = _filter_real(n, "n")
    return n * 2


"""Resultado: factorial de un entero no negativo."""
"""TypeError si n no es entero y ValueErrors si n es menor a 0."""
def factorial(n: int) -> int:
    n = _filter_int(n, "n")
    if n < 0:
        raise ValueError("No existe factorial de enteros negativos")
    return math.factorial(n)


"""Resultado: True si n es primo, False en caso contrario."""
"""TypeError si n no es entero y para n menor que 2."""
def is_prime(n: int) -> bool:
    n = _filter_int(n, "n")
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for f in range(3, r + 1, 2):
        if n % f == 0:
            return False
    return True

"""áximo común divisor (si ambos son 0, no está definido)."""
"""Error si a o b son enteros y error si a y b = 0"""
def gcd(a: int, b: int) -> int:
    a = _filter_int(a, "a")
    b = _filter_int(b, "b")
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) no está definido")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


"""Mínimo común multiplo (si ambos son 0, no está definido)."""
"""Error si a o b son enteros y error si a y b = 0"""
def lcm(a: int, b: int) -> int:
    a = _filter_int(a, "a")
    b = _filter_int(b, "b")
    if a == 0 and b == 0:
        raise ValueError("lcm(0, 0) no está definido")
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


__all__ = ["square", "factorial", "is_prime", "gcd", "lcm"]
