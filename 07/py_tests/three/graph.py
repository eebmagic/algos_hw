import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Node:
    def __init__(self, parentGraph, index, label, labelCost, connectionIndeces):
        self.parentGraph = parentGraph
        self.index = index
        self.label = label
        self.labelCost = labelCost
        self.connections = connectionIndeces

    def getChild(self, index):
        return self.parentGraph.getNode(index)


class Graph:
    def __init__(self, matrix, labels):
        self.matrix = matrix
        self.labels = labels
        self.nodes = []
        for a in range(len(matrix)):
            connections = []
            for b in range(len(matrix)):
                if matrix[a][b] > 0:
                    connections.append(b)
            label = random.choice(labels)
            node = Node(self, a, label, label, connections)
            self.nodes.append(node)

    def getNode(self, index):
        return self.nodes[index]

    def getNodes(self):
        return list(range(0, len(self.matrix)))

    def getWeight(self, a, b):
        return self.matrix[a][b]



def graph(n, m, directed=False, weighted=False):
    '''
    Generates a random graph

    n: number of nodes
    m: max number of edges
    directed: if False, matrix will be symmetrical
    weighted: if False, all matrix values will be 1 or True
    '''
    ## Make these input params?
    edge_prob = 1 + 0.4 # 40% probability of an edge being formed
    weight_min, weight_max = 1, 9

    # default_value = None
    default_value = 0
    out = [[default_value for _ in range(n)] for _ in range(n)]
    edge_count = 0
    
    for y in range(n):
        for x in range(n):
            if edge_count >= m:
                return out 

            if x != y:
                if directed or (not directed and x > y):
                    if random.random() * edge_prob >= 1:
                        edge_count += 1
                        if not weighted:
                            weight = 1
                        else:
                            weight = random.randint(weight_min, weight_max)
                        
                        out[y][x] = weight
                        if not directed:
                            out[x][y] = weight

    return out


def print_matrix(m):
    pairs = [
        ('[[', '['),
        (']]', ']'),
        ('], [', ']\n['),
        ('None', '-')
    ]

    out = str(m)
    for a, b in pairs:
        out = out.replace(a, b)
    print(out)


def deep_count(m, value):
    total = 0
    for row in m:
        total += row.count(value)
    return total 


def draw(matrix, with_weights=False):
    m = np.array(matrix)
    print(m)
    g = nx.DiGraph(m)
    pos = nx.spring_layout(g)
    if with_weights:
        labels = nx.get_edge_attributes(g, 'weight')
        # print(f'LABELS: {labels}')
        # nx.draw_circular(g, with_labels=True)
        # edge_labels = nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        # pos = nx.spring_layout(g)
        pos = nx.circular_layout(g)
        plt.figure()    
        nx.draw(g,pos,edge_color='black',width=1,linewidths=1,\
            node_size=500,node_color='pink',alpha=0.9,\
            labels={node:node for node in g.nodes()})
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels,font_color='red')
        plt.axis('off')
    else:
        nx.draw_circular(g, edge_color='black', width=1, linewidths=1,\
            node_size=500, node_color='pink', alpha=0.9,\
            with_labels=True)
        # nx.draw(g, pos=pos, with_labels=True)
    # nx.draw_shell(g, nlist=[range(len(matrix)//3), range(len(matrix)//3, len(matrix))],
    #     with_labels=True)
    plt.show()



if __name__ == '__main__':
    n = 20
    m = n * 3
    out = graph(n, m, directed=False, weighted=True)
    print_matrix(out)
    draw(out, with_weights=False)
