"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    i_min = 0
    for i in range(1, len(arr)):

        if arr[i_min] > arr[i]:
            i_min = i
#    print(arr)
    return i_min
