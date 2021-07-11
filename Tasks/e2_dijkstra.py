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
    node_list = list(g.nodes)
    distance = {node: float('inf') for node in node_list}
    distance[starting_node] = 0
    weight = 'weight'
    visited = [starting_node]
    distance[starting_node] = 0
    cur = 2
    node = starting_node

    while cur < len(distance):
        edge_list = {}
        for neighbour in g[node]:
            if neighbour not in visited:
                new_dist = distance[node] + g[node][neighbour][weight]
                edge_list[neighbour] = new_dist
            else:
                continue
        if len(edge_list) != 0:
            neighbour = min(edge_list, key=edge_list.get)
            distance[neighbour] = new_dist
            visited.append(neighbour)
            node_list.remove(neighbour)
            node = neighbour
        else:
            node = visited[-cur]
            cur += 1
    return distance
