from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    def slice_(start, stop):
        if elem < start or elem > stop:
            return None
        else:
            mid = start + ((stop - start) // 2)
            if arr[mid] > elem:
                return slice_(start, mid - 1)
            elif arr[mid] < elem:
                return slice_(mid + 1, stop)
            else:
                if arr[mid - 1] == arr[mid] and (mid - 1) >= 0:
                    return mid - 1
                else:
                    return mid

    return slice_(0, len(arr))
