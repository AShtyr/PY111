from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def merge(list_1, list_2):
        list_res = []
        count_1 = count_2 = 0
        for i in range(len(list_1) + len(list_2)):
            if count_1 < len(list_1) and count_2 < len(list_2):
                if list_1[count_1] < list_2[count_2]:
                    list_res.append(list_1[count_1])
                    count_1 += 1
                else:
                    list_res.append(list_2[count_2])
                    count_2 += 1
            elif count_1 == len(list_1):
                list_res.append(list_2[count_2])
                count_2 += 1
            elif count_2 == len(list_2):
                list_res.append(list_1[count_1])
                count_1 += 1
        return list_res

    if len(container) <= 1:
        return container

    middle = len(container) // 2
    list_1 = sort(container[: middle])
    list_2 = sort(container[middle:])
    return merge(list_1, list_2)


