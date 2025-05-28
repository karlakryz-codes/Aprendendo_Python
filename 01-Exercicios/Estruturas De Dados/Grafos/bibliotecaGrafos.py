# Importando a biblioteca NetworkX para criar e manipular grafos
import networkx as nx

# Importando a biblioteca Matplotlib para fazer a visualização do grafo
import matplotlib.pyplot as plt


# Criando um grafo vazio (não direcionado)
grafo = nx.Graph()


# 🔸 Adicionando os vértices (nós) ao grafo
grafo.add_node("a")
grafo.add_node("b")
grafo.add_node("c")  # Adicionando o nó "c"
grafo.add_node("d")


# 🔸 Adicionando as conexões (arestas) entre os nós
grafo.add_edge("a", "b")  # Conecta "a" com "b"
grafo.add_edge("a", "c")  # Conecta "a" com "c"
grafo.add_edge("b", "d")  # Conecta "b" com "d"
grafo.add_edge("c", "d")  # Conecta "c" com "d"
grafo.add_edge("c", "b")  # Conecta "c" com "b"


# 🔍 Obtendo informações sobre o grafo
numeroVertices = grafo.number_of_nodes()  # Conta quantos vértices existem
numeroArestas = grafo.number_of_edges()   # Conta quantas arestas existem


# 🖨️ Exibindo as informações no console
print("Visualizando as ligações de um vértice:", grafo.adj["a"])
# Mostra com quais vértices o vértice "a" está conectado

print("Quantidade de arestas por vértice:", grafo.degree())
# Mostra o grau de cada vértice (quantas conexões ele tem)

print("Quantidade de vértices:", numeroVertices)
# Mostra o total de vértices no grafo

print("Quantidade de arestas:", numeroArestas)
# Mostra o total de arestas no grafo

print("Vértices do grafo:", grafo.nodes())
# Lista todos os vértices do grafo

print("Arestas do grafo:", grafo.edges())
# Lista todas as arestas (as conexões) do grafo



# 🎨 Visualização gráfica do grafo
plt.figure(figsize=(8, 6))  # Define o tamanho da imagem

# Desenha o grafo com várias configurações de aparência
nx.draw(
    grafo,
    with_labels=True,        # Mostra os rótulos (nomes dos nós)
    node_color="skyblue",    # Cor dos nós (círculos)
    node_size=2000,          # Tamanho dos nós
    font_size=15,            # Tamanho da fonte dos rótulos
    font_color="black",      # Cor da fonte dos rótulos
    font_weight="bold",      # Peso da fonte (negrito)
    edge_color="gray"        # Cor das arestas (linhas)
)

# Título da imagem
plt.title("Visualização do Grafo", fontsize=18)

# Exibe o gráfico na tela
plt.show()
