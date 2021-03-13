import graph
import random

def algo(matrix, labels, labelCosts, start, target):
    g = graph.Graph(matrix, labels)
    nodes = g.getNodes()
    costToReach = {n: float('inf') for n in nodes}
    previousNode = {n: None for n in nodes}

    costToReach[start] = 0

    q = set(nodes)
    print(q)
    while len(q) > 0:
        costs = {n:costToReach[n] for n in q}
        u = min(costs, key=lambda n: costs[n])
        print(f'removing {u} from {q}')
        q.remove(u)
        if u == target:
            print(f'costs: {costToReach}')
            print(f'previousNodes: {previousNode}')
            return

        u = g.getNode(u)
        # print(u.index, u.connections)
        for index in u.connections:
            if index in q:
                neighbor = g.getNode(index)
                if neighbor.label == u.label:
                    alt = costToReach[u.index] + labelCosts[u.label]
                else:
                    alt = costToReach[u.index] + g.getWeight(u.index, index)

                if alt < costToReach[index]:
                    costToReach[index] = alt
                    previousNode[index] = u.index

    print(f'costs: {costToReach}')
    print(f'previousNodes: {previousNode}')


if __name__ == '__main__':
    nodes = 10
    edges = nodes * 3
    g = graph.graph(nodes, edges, weighted=True)
    k = nodes
    labels = list(range(1, k//3))
    costs = {x:x for x in labels}

    start = random.randint(0, nodes-1)
    while sum(g[start]) <= 0:
        start = random.randint(0, nodes-1)

    end = start
    while end == start or sum(g[end]) <= 0:
        end = random.randint(0, nodes-1)

    graph.print_matrix(g)
    print(start, end)

    algo(g, labels, costs, start, end)
    graph.draw(g, with_weights=True)
