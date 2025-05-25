# Função para entrada de valores
def ler_valores():
    quantidade = int(input("Quantos valores deseja inserir? "))
    valores = []
    for i in range(quantidade):
        valor = float(input(f"Valor {i+1}: "))
        valores.append(valor)
    return valores

#função para calcular a media
def calcular_media(lista):
    return sum(lista)/len(lista)    

#função para calcular desvio medio absoluto
def desvio_medio_absoluto(lista,media):
    desvios = [abs(x-media)for x in lista]
    return sum(desvios)/len(desvios)

def main():
  n=10
  valores = []
  media = None
  
  while True:
       print("\n--- MENU ---")
       print("1 - Inserir valores")
       print("2 - Calcular média aritmética")
       print("3 - Calcular desvio médio absoluto")
       print("4 - Sair")
       opcao = input("Escolha uma opção: ")
       
       if opcao == '1':
           valores = ler_valores()
           media = None # Zera a média anterior
           print("Valores registrados com sucesso!")
           
       elif opcao == '2':
           if valores:
               media=calcular_media(valores)
               print(f"A média aritmética é {media:.2f}") 
           else:
               print("Por favor insira os valores primeiro (opção 1).")    
               
       elif opcao =='3':
            if valores:
                if media is None:
                    media=calcular_media(valores)
                desvio= desvio_medio_absoluto(valores,media)    
                print(f"O desvio médio absoluto é {desvio:.2f}")
            else:
                print("Por favor insira os valores primeiro (opção 1).")  
                
       elif opcao=='4':  
           print("Saindo do programa. Até mais!")    
           break
       else:
           print("Opção inválida. Tente novamente.")  
           
if __name__ == "__main__":
    main()           
            
                    
           
           
           
           
           
           
           
           
  
