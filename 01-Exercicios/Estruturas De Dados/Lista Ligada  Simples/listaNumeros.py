import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pilha:
    def __init__(self):
        self.itens = []
        
    def empilhar(self, item):
        self.itens.append(item)  
        
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0
          
class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None
        
class ListaLigada:
    def __init__(self):
        self.cabeca = None
       
    def adicionar(self, numero):   
        novo_no = No(numero)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca   
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no   
            
    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.numero, end=" -> ")
            atual = atual.proximo
        print(None)  
        
    def tamanho(self):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador
    
    def remover(self, numero, pilha=None): 
        atual = self.cabeca
        anterior = None
        while atual and atual.numero != numero:
            anterior = atual
            atual = atual.proximo
        if atual:
            if anterior is None:
                self.cabeca = atual.proximo
            else:
                anterior.proximo = atual.proximo
                 
            if pilha:
                pilha.empilhar(numero)     
            print(f"Número {numero} removido.")
        else:
            print("Número não encontrado.")   
            
    def buscar(self, numero):
        atual = self.cabeca  
        while atual is not None:
            if atual.numero == numero:
                return True
            atual = atual.proximo
        return False   
    
    def desfazer_remocao(self, pilha):
        if pilha.esta_vazia():
            print("Nenhuma remoção para desfazer.")
            return
        numero = pilha.desempilhar()
        self.adicionar(numero)
        print(f"Número {numero} restaurado na lista.")
            
pilha_removidos = Pilha()    
lista = ListaLigada()

while True:
    print("\n----- MENU -----")
    print("1 - Adicionar número")
    print("2 - Remover número")
    print("3 - Buscar número")
    print("4 - Imprimir lista")
    print("5 - Ver tamanho da lista")
    print("6 - Desfazer última remoção")
    print("7 - Sair")

    opcao = input("Escolha uma opção:\n ")
    
    if opcao == "1":
        numero = int(input("Digite o número para adicionar: "))
        lista.adicionar(numero)
        print("Número adicionado com sucesso!")
        input("\nPressione ENTER para continuar...")
        
    elif opcao == "2":
        numero = int(input("Digite o número para remover: "))
        lista.remover(numero, pilha_removidos)
        input("\nPressione ENTER para continuar...")
        
    elif opcao == "3":
        numero = int(input("Digite o número para buscar: "))
        if lista.buscar(numero):
            print(f"Número {numero} encontrado na lista.")
        else:
            print(f"Número {numero} não encontrado na lista.")
        input("\nPressione ENTER para continuar...")
        
    elif opcao == "4":
        print("Lista Atual:")
        lista.imprimir() 
        input("\nPressione ENTER para continuar...")  
        
    elif opcao == "5":
        tamanho = lista.tamanho()
        if tamanho == 0:
            print("A lista está vazia.")
        else:
            print(f"Tamanho da lista: {tamanho}")  
        input("\nPressione ENTER para continuar...")
       
    elif opcao == "6":
        lista.desfazer_remocao(pilha_removidos)
        input("\nPressione ENTER para continuar...")
         
    elif opcao == "7":
        print("Saindo do sistema. Até logo!")
        break     
       
    else:
        print("Opção inválida. Escolha novamente.")
        input("\nPressione ENTER para continuar...")      
