from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    nodes = list(set([g[i][1] for i in range(len(g))]))

    list_dict = []
    for i in nodes:
        list_node = []
        list_weight = []
        for j in range(len(g)):
            if g[j][0] == i:
                list_node.append(g[j][1])
                list_weight.append(g[j][2])
            dict_node = {n: w for (n, w) in zip(list_node, list_weight)}
        list_dict.append(dict_node)
    distance = {node: dict_ for (node, dict_) in zip(nodes, list_dict)}

    until = {node: None for node in nodes}
    already = {}
    start_dist = 0
    until[starting_node] = start_dist

    while True:
        for neighbour, dist in distance[starting_node].items():
            if neighbour not in until:
                continue
            next_dist = start_dist + dist
            if until[neighbour] is None or until[neighbour] > next_dist:
                until[neighbour] = next_dist
        already[starting_node] = start_dist
        del until[starting_node]
        if not until:
            break
        next_nodes = [node for node in until.items() if node[1]]
        starting_node, start_dist = sorted(next_nodes, key=lambda x: x[1])[0]
    return already

