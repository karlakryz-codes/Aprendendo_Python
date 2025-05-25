def soma(numero1,numero2):
    print(f" {numero1} + {numero2} = {numero1 + numero2}")
    
def subtracao(numero1,numero2):
    print(f" {numero1} - {numero2} = {numero1 - numero2}")
    
def multiplicacao(numero1,numero2):
    print(f" {numero1} x {numero2} = {numero1 * numero2}")  
    
def divisao(numero1,numero2):
    if numero2 ==0:
        print("Erro divisão por zero não é permitida!")
    else:    
        print(f" {numero1} / {numero2} = {numero1 / numero2:}")  
        
while True:
    opcao = int (input(
        "Escolha uma opção:\n"
        "1-Soma\n"
        "2-Subtração\n"
        "3-Multiplicação\n"
        "4-Divisão\n"
        "5-Sair\n"
        "Digite a opção :\n"
     ))
    
    if opcao == 5:
        print("Encerrando o programa. Até logo!")
        break
    
    if  opcao in [ 1,2,3,4]:
        numero1=int( input("Digite o primeiro número : "))    
        numero2= int( input("Digite o segundo número : "))
        
        if opcao == 1:
            soma(numero1,numero2)    
        elif opcao == 2:
            subtracao(numero1,numero2)   
        elif opcao == 3:
            multiplicacao(numero1,numero2)     
        elif opcao == 4:
            divisao(numero1,numero2  )
    else:
            print("Opção inválida")      
        
                

 

  
    



    


multiplicacao(numero1,numero2)