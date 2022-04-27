
from unittest import result


def es_par(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False

def test_positivo():
    result = es_par(2, 4)
    assert result

def test_negative():
    result = es_par(3, 9)
    assert not result

def test_menor_par():
    result = es_par(2, 0)
    assert result

def test_impar():
    result = es_par(5, 15)
    assert not result

def test_impar_negative():
    result = es_par(5, 15)
    assert result

