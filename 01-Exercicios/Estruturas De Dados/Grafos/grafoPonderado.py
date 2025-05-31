import networkx as nx 
import matplotlib.pyplot as plt

G =nx.Graph()
arestas=[
    (1,2,3),(1,5,4),
    (2,3,1),(2,6,1,),
    (3,4,2),(3,6,3),
    (4,5,9),
    (5,6,4)
]

G.add_weighted_edges_from(arestas)

plt.figure(figsize=(8,6),facecolor="black")

pos = nx.spring_layout(G)

nx.draw_networkx_edges(G,pos,edge_color= "red",width=2)  #arestas
nx.draw_networkx_nodes(G,pos,node_color="blue",node_size=500)  #vertices

nx.draw_networkx_labels(G,pos)

labels=nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=10) #pesos

plt.title("Gráfico Ponderado " ,color="white")
plt.axis("off")
plt.show()