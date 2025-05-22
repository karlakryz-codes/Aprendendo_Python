VetClasse = [] #Cria uma lista vazia.

# Leitura das notas
for x in range(10): #Loop de 10 vezes.
    nota = float(input(f"Nota {x + 1}: ")) #Lê a nota do usuário.
    VetClasse.append(nota) #Adiciona a nota na lista.
    
# Cálculo da média
media = sum(VetClasse) / len(VetClasse) #Soma todos os valores e divide pelo total para calcular a média.

# Contagem de notas acima da média
nota_acima = sum(1 for nota in VetClasse if nota > media) #Conta quantas notas são maiores que a média.

# Resultado
print(f"Número de notas acima da média: {nota_acima}")
            