from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input gstart_noderaph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    stack, already = [start_node], []
    while stack:
        node = stack.pop()
        if node in already:
            continue
        already.append(node)
        for neighbor in g.neighbors(node):
            stack.append(neighbor)
    return already
































