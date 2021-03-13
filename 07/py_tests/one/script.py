import graph
import networkx as nx
import numpy as np


def algo(graph, edges):
    included_nodes = set()
    edges = sorted(edges, key=lambda x: x[0])
    print(edges)



directed = graph.graph(10, 20, directed=True, weighted=True)
print(str(directed).replace('], [', ']\n['))
edges = []
# (weight, (from, to))
for a in range(len(directed)):
    for b in range(len(directed)):
        weight = directed[a][b]
        if weight > 0:
            edges.append((weight, (a, b)))

print(edges)
algo(directed, edges)
