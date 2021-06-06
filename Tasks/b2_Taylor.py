"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    f = 1
    exp = 1
    dx = x
    i = 1
    while dx > 0.0001:
        f *= i
        dx = x ** i / f
        exp += dx
        i += 1
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    f = 1
    st = 0
    i = 1
    dx = x
    z = 1
    while dx > 0.0001:
        f *= (2 * i + 1) * 2 * i
        dx = x ** (2 * i + 1) / f
        st += dx * z
        i += 1
        z *= -1
    return x - st
