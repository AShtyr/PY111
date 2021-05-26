"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
pr_queue = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    pr_queue.append((priority, elem))
    pr_queue.sort(key=lambda x: x[0])



def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(pr_queue) != 0:
        return pr_queue.pop(0)[1]



def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(pr_queue) > ind:
        return pr_queue[ind][1]
    pr_queue.sort(key=lambda x: x[0])




def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    pr_queue.clear()

