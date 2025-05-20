lista = []

for i in range(1, 11):  # Começa do 1 até 10
    print(f"Digite o elemento da posição {i}:")
    dado = int(input())
    lista.append(dado)

print("\nLista preenchida com sucesso!\n")

#for i in range(1, 11):  # Mesma lógica na hora de mostrar vai de 1 até 10
    #print(f"O elemento da posição {i} é {lista[i - 1]}") # porque mesmo que você exiba como se começasse do 1, a lista internamente 
    #começa no índice 0

for i in range(1, 11,2):  # Mesma lógica na hora de mostrar vai de 1 até 10
    print(f"O elemento da posição {i} é {lista[i - 1]}") # porque mesmo que você exiba como se começasse do 1, a lista internamente 
    #começa no índice 0
    