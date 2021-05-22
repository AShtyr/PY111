"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

pr_que = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    pr_que.append((priority, elem))
    pr_que.sort(key=lambda x: x[0], reverse=False)



def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(pr_que) != 0:
        return pr_que.pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """




    return


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return None
