import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()
arestas=[
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 4),
    (3, 6),
    (4, 5),
    (5, 6)
    
]

G.add_edges_from(arestas) #adicionado as arestas

plt.figure(figsize=(6,6),facecolor="#06010F") #tamanho em polegadas e cor da imagem
pos=nx.spring_layout(G) #organizando layout

nx.draw_networkx_edges(G,pos,edge_color="#FF00FF",width=5) #arestas
nx.draw_networkx_nodes(G,pos,node_color="#36454F",node_size=500) #vertices
nx.draw_networkx_labels(G,pos) #rotulos

plt.title("Grafo Não Direcionado")
plt.axis("off")
plt.show()

