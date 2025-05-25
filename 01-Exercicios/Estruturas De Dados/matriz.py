mat = []

for i in range(3):           # Percorre as linhas (0,1,2)
    linha = []               # Cria uma lista vazia para armazenar a linha atual
    for j in range(3):       # Percorre as colunas (0,1,2)
        print(f"Insira o elemento da linha {i + 1}, coluna {j + 1}:")
        dado = int(input())  # Recebe o número digitado pelo usuário
        linha.append(dado)   # Adiciona o número na lista da linha
    mat.append(linha)        # Depois que a linha está completa, adiciona ela à matriz
    
for linha in mat:               # Para cada linha na matriz
    for elemento in linha:      # Para cada elemento dessa linha
        print(elemento, end="\t")  # Imprime o elemento seguido de uma tabulação (espaço maior)
    print()                    # Quebra de linha, para a próxima linha da matriz ser impressa abaixo
    
