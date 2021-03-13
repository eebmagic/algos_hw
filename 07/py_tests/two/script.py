import graph
import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_nodes_from([0, 1, 2, 3, 4])
g.add_edge(0, 1, weight=1)
g.add_edge(0, 2, weight=0)
g.add_edge(1, 2, weight=1)
g.add_edge(1, 3, weight=1)
g.add_edge(2, 3, weight=0)

pos = nx.spring_layout(g)
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

# print(g.nodes)
# print(g.edges)
# plt.show()


k = 1
x = 0
