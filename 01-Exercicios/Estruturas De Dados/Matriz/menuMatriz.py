import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_matriz():
    print("*" * 30)
    print("Matriz Digitada ✅")
    for linha in matriz:
        for elemento in linha:
            print(f'{elemento:^5}', end=' ')
        print()  
    print("*" * 30)    


def soma_diagonal(matriz):
    n = len(matriz)
    soma_principal = 0
    soma_secundaria = 0
    
    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n - 1 - i]
    
    return soma_principal, soma_secundaria


def soma_elementos(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma        


def multiplicar_matriz(matriz, escalar):
    nova_matriz = []
    for linha in matriz:
        nova_linha = [elemento * escalar for elemento in linha]
        nova_matriz.append(nova_linha)
    return nova_matriz


# Criando a matriz
matriz = []

n = int(input("Digite o tamanho da Matriz N x N: "))

for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)


# Loop do Menu
while True:
    limpar_tela()

    opcao = int(input(
        "Escolha uma opção:\n"
        "1 - Mostrar matriz\n"
        "2 - Somar diagonal principal\n"
        "3 - Somar diagonal secundária\n"
        "4 - Somar todos os elementos\n"
        "5 - Multiplicar matriz por um escalar\n"
        "6 - Sair\n"
        "Digite a opção: "
    ))
    
    if opcao == 6:
        print("Encerrando o programa. Até logo! 👋")
        break

    elif opcao == 1:
        mostrar_matriz()
        input("\nPressione ENTER para continuar...")

    elif opcao == 2:
        soma_principal, _ = soma_diagonal(matriz)
        print(f"Soma da diagonal principal ➡️  {soma_principal}")
        input("\nPressione ENTER para continuar...")

    elif opcao == 3:
        _, soma_secundaria = soma_diagonal(matriz)
        print(f"Soma da diagonal secundária ➡️  {soma_secundaria}")
        input("\nPressione ENTER para continuar...")

    elif opcao == 4:
        soma = soma_elementos(matriz)
        print(f"A soma dos elementos ➡️  {soma}")
        input("\nPressione ENTER para continuar...")

    elif opcao == 5:
        escalar = int(input("Informe o multiplicador: "))
        matriz = multiplicar_matriz(matriz, escalar)
        print(f"A matriz foi multiplicada por {escalar} com sucesso! ✅")
        mostrar_matriz()
        input("\nPressione ENTER para continuar...")

    else:
        print("🚫 Opção inválida.")  
        input("\nPressione ENTER para continuar...") 

    
        
    
        
    
        
         
            
            
        
      


  
    
      
   


     
    
        
    