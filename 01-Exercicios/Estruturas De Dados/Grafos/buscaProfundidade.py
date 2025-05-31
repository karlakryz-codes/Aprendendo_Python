# Importação das bibliotecas necessárias
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos
import networkx as nx            # Biblioteca para criação e manipulação de grafos
from matplotlib.backends.backend_pdf import PdfPages  # Permite salvar os gráficos em PDF

# Função que desenha o grafo na tela e salva como imagem e PDF
def desenharGrafo(colors, weights):
    global contadorFigura  # Controla o número das imagens salvas

    # Desenha o grafo
    nx.draw(
        G,
        with_labels=True,          # Mostra os rótulos dos nós
        pos=posicionamento,        # Define a posição dos nós no gráfico
        edge_color=colors,         # Define a cor das arestas
        width=list(weights),       # Define a espessura das arestas
        node_color='red'           # Cor dos nós
    )

    pdf.savefig()  # Salva o gráfico no arquivo PDF

    nomeImagem = "Grafo" + str(contadorFigura) + ".jpg"  # Define o nome da imagem
    contadorFigura += 1  # Incrementa o contador de imagens

    plt.savefig(nomeImagem)  # Salva como arquivo JPG
    plt.show()               # Exibe o grafo na tela


# Função que desenha o grafo inicial, com todas as arestas pretas e peso 1
def desenhoInicialGrafo():
    global weights, posicionamento  # Torna essas variáveis globais

    for n1, n2 in arestas:  # Percorre todas as arestas
        G.add_edge(
            n1, n2,
            label=(n1 + "->" + n2),  # Label da aresta
            color="black",           # Cor inicial (preta)
            weight=1                 # Peso inicial (espessura da linha)
        )

    colors, weights = definirAtributos()       # Obtém cores e pesos atuais
    posicionamento = nx.planar_layout(G)       # Define a posição dos nós no plano
    desenharGrafo(colors, weights)             # Desenha o grafo inicial


# Função que obtém as cores e pesos atuais das arestas
def definirAtributos():
    colors = nx.get_edge_attributes(G, 'color').values()   # Coleta as cores das arestas
    weights = nx.get_edge_attributes(G, 'weight').values() # Coleta os pesos (espessura) das arestas
    return colors, weights  # Retorna as listas


# Função que atualiza uma aresta, mudando sua cor e espessura
def atualizarDesenho(v1, v2):
    global corRedesenho, contadorCor, controleCor  # Usa variáveis globais de controle

    controleCor = True  # Ativa o controle
    G.get_edge_data(v1, v2)["color"] = corRedesenho[contadorCor]  # Atualiza a cor da aresta
    G.get_edge_data(v1, v2)["weight"] = 4  # Aumenta a espessura da aresta para 4

    colors, weights = definirAtributos()  # Atualiza listas de cores e pesos
    desenharGrafo(colors, weights)        # Redesenha o grafo atualizado


# Inicializa variáveis globais usadas durante a execução
def inicializaVariaveis():
    global valorProfundidadeEntrada, valorProfundidadeSaida, ProfundidadeEntradaSaida
    global verticesPai, controleVertices, demarcadores
    global verticeComSaidaValidas, corRedesenho, contadorCor, controleCor
    global niveis

    # Inicializa os valores
    valorProfundidadeEntrada = 0
    valorProfundidadeSaida = 0
    ProfundidadeEntradaSaida = {}   # Guarda a profundidade de entrada e saída de cada nó
    verticesPai = {}                # Guarda quem é o pai de cada nó
    niveis = {}                     # Guarda o nível de cada nó
    controleVertices = {}           # Controle dos vértices
    demarcadores = set()            # Marca vértices especiais
    verticeComSaidaValidas = set()  # Vértices com saídas válidas
    corRedesenho = ["red", "green", "blue", "gray"]  # Cores usadas para redesenhar arestas
    contadorCor = 0                 # Índice para selecionar a cor da lista
    controleCor = True              # Controle para evitar incrementos indevidos


# Função principal de busca em profundidade (DFS)
def buscaEmProfundidade(vertices, arestas, verticeGrafo):
    inicializaVariaveis()  # Inicializa variáveis globais

    grafo = {}  # Dicionário que representa o grafo (lista de adjacência)

    # Preenche o grafo com os vértices e suas conexões
    for v in vertices:
        grafo[v] = []

        for a in arestas:
            if v == a[0]:  # Se v é o nó de origem da aresta
                grafo[v].append(a[1])  # Adiciona o destino da aresta

    # Inicializa controle dos vértices
    for vertice in grafo:
        controleVertices[vertice] = vertice

    verticesPai[verticeGrafo] = None  # O vértice raiz não possui pai

    # Inicia a busca recursiva
    quantidadeFilhosRaiz = procuraProximoVertice(grafo, verticeGrafo, 1)

    # Verifica se a raiz deve estar no conjunto de vértices com saída válida
    if quantidadeFilhosRaiz <= 1:
        verticeComSaidaValidas.remove(verticeGrafo)


# Função recursiva que executa a busca em profundidade
def procuraProximoVertice(grafo, verticeGrafo, nivel):
    global valorProfundidadeEntrada, valorProfundidadeSaida, contadorCor

    valorProfundidadeEntrada += 1
    ProfundidadeEntradaSaida[verticeGrafo] = [valorProfundidadeEntrada, None]  # Marca entrada
    niveis[verticeGrafo] = nivel  # Guarda o nível do vértice

    contadorFilhos = 0  # Conta quantos filhos o vértice possui

    for proximoVertice in grafo.get(verticeGrafo):
        if not ProfundidadeEntradaSaida.get(proximoVertice):
            verticesPai[proximoVertice] = verticeGrafo
            contadorFilhos += 1

            atualizarDesenho(verticeGrafo, proximoVertice)  # Atualiza o desenho da aresta
            procuraProximoVertice(grafo, proximoVertice, nivel + 1)  # Chamada recursiva

            # Atualiza o controle de vertices
            if niveis[controleVertices[proximoVertice]] < niveis[controleVertices[verticeGrafo]]:
                controleVertices[verticeGrafo] = controleVertices[proximoVertice]

            if proximoVertice in demarcadores:
                verticeComSaidaValidas.add(verticeGrafo)

        else:
            if not ProfundidadeEntradaSaida[proximoVertice][1]:
                if verticesPai[verticeGrafo] != proximoVertice:
                    if niveis[proximoVertice] < niveis[controleVertices[verticeGrafo]]:
                        controleVertices[verticeGrafo] = proximoVertice

    valorProfundidadeSaida += 1
    ProfundidadeEntradaSaida[verticeGrafo][1] = valorProfundidadeSaida  # Marca saída

    # Verifica se o vértice é um demarcador
    if controleVertices[verticeGrafo] in (verticeGrafo, verticesPai[verticeGrafo]):
        demarcadores.add(verticeGrafo)

        if controleCor:
            contadorCor += 1
            controleCor = False

    return contadorFilhos  # Retorna o número de filhos do vértice


# Cria o grafo direcionado
G = nx.DiGraph()

# Contador para nomear figuras
contadorFigura = 1

# Cria o arquivo PDF para salvar os gráficos
pdf = PdfPages('GrafoPassoAPasso.pdf')

# Define os vértices do grafo
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Define as arestas do grafo (origem, destino)
arestas = [
    ('a', 'b'),
    ('a', 'e'),
    ('b', 'c'),
    ('e', 'd'),
    ('e', 'f'),
    ('c', 'e'),
    ('f', 'd'),
    ('a', 'g'),
    ('g', 'd')
]

# Desenha o grafo inicial
desenhoInicialGrafo()

# Executa a busca em profundidade a partir do vértice 'a'
buscaEmProfundidade(vertices, arestas, "a")

# Fecha o arquivo PDF, salvando os gráficos
pdf.close()
