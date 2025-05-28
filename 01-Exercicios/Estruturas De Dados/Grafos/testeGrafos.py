from collections import defaultdict

class grafo(object):
    def __init__(self, arestas, direcionado=False):
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adicionar_aresta(arestas)

    def get_vertice(self):
        return list(self.adj.keys())

    def get_aresta(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adicionar_aresta(self, arestas):
        for u, v in arestas:
            self.adiciona_ligacao(u, v)

    def adiciona_ligacao(self, u, v):
        self.adj[u].add(v)
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]


# Dados de entrada 
arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A')]

criagrafo = grafo(arestas, direcionado=True)

print(criagrafo.adj)

print(criagrafo.get_vertice())

print(criagrafo.get_aresta())

print(criagrafo.existe_aresta('A', 'B'))

print(criagrafo.existe_aresta('E', 'C'))
