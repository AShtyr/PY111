from typing import Hashable, Mapping, Union
import networkx as nx
import math


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    distance = {starting_node: 0}
    node_list = list(g.nodes)
    weight = 'weight'

    if starting_node in node_list:
        node_list.remove(starting_node)


    node = starting_node

    while node_list:
        prev_dist = float('inf')
        for neighbour in g[node]:
            distance[neighbour] = g[node][neighbour][weight]
            if prev_dist > distance[node] + g[node][neighbour][weight]:
                prev_dist = distance[starting_node] + g[node][neighbour][weight]
                node = neighbour
        node_list.remove(node)

    return distance



































































































