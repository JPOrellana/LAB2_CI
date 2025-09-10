# test_funciones.py
import pytest
from funciones import square, factorial, is_prime, gcd, lcm


def test_square():
    # Casos normales
    assert square(5) == 25
    assert square(-3) == 9
    # Error: tipo no válido
    with pytest.raises(TypeError):
        square("texto")


def test_factorial():
    # Casos normales
    assert factorial(0) == 1
    assert factorial(5) == 120
    # Error: número negativo
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_prime():
    # Casos normales
    assert is_prime(2) is True
    assert is_prime(13) is True
    # Casos que no son primos
    assert is_prime(1) is False
    assert is_prime(9) is False
    # Error: tipo no válido
    with pytest.raises(TypeError):
        is_prime(3.5)


def test_gcd():
    # Casos normales
    assert gcd(12, 18) == 6
    assert gcd(7, 13) == 1
    assert gcd(0, 9) == 9
    # Error: ambos ceros
    with pytest.raises(ValueError):
        gcd(0, 0)


def test_lcm():
    # Casos normales
    assert lcm(12, 18) == 36
    assert lcm(7, 13) == 91
    assert lcm(0, 5) == 0
    # Error: ambos ceros
    with pytest.raises(ValueError):
        lcm(0, 0)
