# Função para imprimir a tabuada de um número
def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar o número para o qual a tabuada será exibida
numero = int(input("Digite um número para ver a tabuada: "))

# Chamar a função tabuada
tabuada(numero)
