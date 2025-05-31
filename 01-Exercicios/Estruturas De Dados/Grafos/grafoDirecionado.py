import networkx as nx
import matplotlib.pyplot as plt


G=nx.DiGraph()
arestas=[
    (1, 2, 5),
    (1, 3, 3),
    (2, 4, 2),
    (2, 5, 4),
    (3, 5, 7),
    (4, 6, 1),
    (5, 6, 6),
    (5, 7, 8),
    (6, 7, 3)
]

G.add_weighted_edges_from(arestas)
plt.figure(figsize=(8,6),facecolor="pink")
pos=nx.spring_layout(G)

nx.draw_networkx_edges(G,pos,width=2,edge_color="black",arrows=True,arrowsize=1,arrowstyle= "-|>")
nx.draw_networkx_nodes(G,pos,node_size=500,node_color="green",node_shape="s")
nx.draw_networkx_labels(G,pos)

labels=nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_color="blue")

plt.title("Grafo Direcionado")
plt.axis("off")
plt.show()