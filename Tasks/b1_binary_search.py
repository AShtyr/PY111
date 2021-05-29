from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    a = 0
    b = len(arr)-1
    mid = (a+b)//2

    while a <= b:
        if arr[mid] == elem:
            break
        else:
            if elem < arr[mid]:
                b = mid - 1
                mid = (a + b) // 2
            else:
                a = mid + 1
                mid = (a + b) // 2
    else:
        return None


    while mid > 0 and arr[mid-1] == elem:
        mid -= 1
    return mid


