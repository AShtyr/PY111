def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """

    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    print(n)
    return factorial_recursive(n-1)*n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    for i in range(n):
        if i == 0:
            return 1
        f = i*(i+1)
        return



