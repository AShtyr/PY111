from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def separation(start, stop):
        middle = (start + stop) // 2
        i, j = start - 1, stop + 1
        separator = container[middle]
        while True:
            i += 1
            while container[i] < separator:
                i += 1
            j -= 1
            while container[j] > separator:
                j -= 1

            if i >= j:
                return j
            container[i], container[j] = container[j], container[i]

    def for_sort(list_, start, stop):
        if start < stop:
            separation_ind = separation(start, stop)
            for_sort(list_, start, separation_ind)
            for_sort(list_, separation_ind + 1, stop)

    for_sort(container, 0, len(container) - 1)

    return container
