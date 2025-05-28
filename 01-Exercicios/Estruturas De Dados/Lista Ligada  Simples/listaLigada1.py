class No: #Cria uma classe Nó, que representa cada elemento da lista.
   def __init__(self,dado): #É o construtor, chamado sempre que você cria um novo nó.
       self.dado = dado #recebe o valor (dado) que você quer guardar.
       self.proximo = None #Cria uma ligação, essa referência será usada para apontar para o próximo nó.
       
class ListaLigada:
    def __init__(self):
        self.cabeca = None   #lista começa vazia,o primeiro nó se torna a cabeça da lista.
        
    def adicionar(self,dado):
        novo_no = No(dado)  #Cria um novo nó com o dado que você quer inserir.
        if self.cabeca is None: #Se a lista estiver vazia, esse novo nó vira a cabeça da lista.
            self.cabeca = novo_no
        else:
            atual= self.cabeca 
            while atual.proximo:  ##Isso faz ele chegar no último nó da lista.
                atual= atual.proximo
            atual.proximo= novo_no  #O último nó, que tinha proximo = None, agora aponta para o novo nó.


            
    def exibir(self):
        atual=self.cabeca
        while atual: #Enquanto houver um nó
            print(atual.dado, end=" -> ")   #Mostra o valor do nó
            atual= atual.proximo #Anda para o próximo
        print("None")   #Quando acabar, imprime "None" para indicar o final da lista.               
                
                
lista = ListaLigada() # Cria a lista (vazia)
lista.adicionar(10) # Adiciona o 10
lista.adicionar(20) # Adiciona o 20
lista.adicionar(30) # Adiciona o 30

lista.exibir()     # Exibe a lista            