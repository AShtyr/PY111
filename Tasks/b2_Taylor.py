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
    exp = 1 + x
    dx = x  # increment
    i = 2

    while dx > 0.0001:
        dx *= x / i
        exp += dx
        i += 1
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    st = 0
    i = 1
    dx = x  # increment
    z = 1
    while dx > 0.0001:
        den = (2 * i + 1) * 2 * i
        dx *= x * x / den
        st += dx * z
        i += 1
        z *= -1
    return x - st
