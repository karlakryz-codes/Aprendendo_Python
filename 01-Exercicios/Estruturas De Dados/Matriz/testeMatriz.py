#Definindo tamanho matriz 3 linhas e 3 colunas → matriz 3x3 (quadrada).
linhas = 3
colunas = 3

# Criação de uma lista vazia, que servirá para armazenar toda a matriz.
matriz = []

for i in range(linhas): # vai percorrer as linhas da matriz.
    linha = []  #cria uma lista vazia chamada linha.Vai armazenar os valores (os elementos das colunas) daquela linha específica da matriz.
    for j in range(colunas): # vai percorrer as colunas da linha
        valor = int (input(f"Digite o valor para [{i}][{j}]:"))
        linha.append(valor) #valor digitado é adicionado na lista linha
    matriz.append(linha)    #lista linha é adicionada na lista principal matriz.
   
print("Matriz Digitada:")
for linha in matriz: #Percorre cada linha da matriz.
    for elemento in linha: #Percorre cada  coluna
        print(f'{elemento:^5}', end=' ')  # ^5 centraliza em um espaço de 5 caracteres
        #end=' ' impede a quebra de linha automática
    print()  # Quebra de linha
     
     
     #Loop externo → linhas (i)
        #↳ Loop interno → colunas (j)
           #↳ Input do valor
           #↳ Adiciona na linha
        #↳ Adiciona a linha na matriz