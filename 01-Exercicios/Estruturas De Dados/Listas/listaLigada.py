class Node: #criando um tipo de objeto chamado Node (nó).
    def __init__(self,valor): #passa um valor ao criar o nó, e esse valor será guardado dentro dele.
        self.valor = valor #Armazena o valor passado
        self.proximo = None #esse nó não está ligado a nenhum outro.Mais pra frente, você pode fazer ele apontar para o próximo nó da lista.
        
        
class ListaLigada:
    def __init__(self):#def → você está definindo uma função.__init__ → é o nome da função especial de inicialização.é uma referência ao próprio objeto que está sendo criado
        self.cabeca = None #"A lista começa vazia."
        
    def mostrar(self): #cria função para mostrar na tela todos os nós da lista
        atual = self.cabeca #A variável atual recebe o primeiro nó da lista
        pos = 0 #variável pos, que serve para marcar a posição de cada nó
        
        while atual: #enquanto existir um nó,vai continuar executando o que estiver dentro do bloco while
         print(f"Posição {pos}| Nó atual: [{atual.valor}] (id:{id(atual)}) -> Próximo: {id(atual.proximo) if atual.proximo else None}")    
        
         #Posição {pos} → A posição do nó na lista/[{atual.valor}] → O valor que esse nó guarda/id:{id(atual)} → O endereço (na memória) do nó atual/
         #-> Próximo: → O endereço do próximo nó/id(objeto) → mostra o endereço na memória do objeto.
        
         atual = atual.proximo #faz atual apontar para o próximo nó da lista
         pos += 1  #Soma 1 na posição, porque ele já passou para o próximo nó.
        print("Fim da lista\n")
        
    def inserir_ordenado(self,valor): #função vai inserir um novo nó na lista em ordem crescente
        novo_no = Node(valor) #cria um novo nó da lista usando a classe Node(armazena o id do objeto)
        
        if self.cabeca is None or valor < self.cabeca.valor: 
            #self.cabeca is None=A lista está vazia?se for verdade que não tem nenhum nó, o novo nó vai ser o primeiro.
            #valor < self.cabeca.valor =O valor que quero inserir é menor do que o valor do primeiro nó da lista?
            #Se for menor, significa que o novo valor deve ficar antes do atual primeiro nó para manter a ordem.
            
            novo_no.proximo =self.cabeca  #O próximo do novo nó será o antigo primeiro nó da lista.
            self.cabeca = novo_no  #O novo nó agora é o primeiro nó da lista.
            return  # Interrompe a função porque o nó já foi inserido corretamente no início da lista
            
        atual = self.cabeca  #“olhar” a lista desde o primeiro nó.
        while atual.proximo and atual.proximo.valor < valor: #você está andando na lista até achar o lugar certo para inserir o novo nó,
            #onde o próximo nó tem valor maior ou igual ao valor que você quer colocar.
            #atual.proximo: existe um próximo nó depois do nó que você está olhando agora.
            #atual.proximo.valor < valor: o valor do próximo nó é menor que o valor que você quer inserir.
            
            atual = atual.proximo     #Atualiza a variável atual para apontar para o próximo nó.
            
        novo_no.proximo = atual.proximo  #novo nó vai “apontar” para o nó que estava logo após o atual
        atual.proximo = novo_no     #novo nó vai “apontar” para o nó que estava logo após o atual
        
lista = ListaLigada() #Cria uma nova lista vazia.
lista.inserir_ordenado(30) #A lista está vazia (cabeca is None), então 30 entra como primeiro elemento.
lista.inserir_ordenado(10) #10 é menor que 30, então entra no início da lista.
lista.inserir_ordenado(20) #Começa no 10. Como 20 > 10, avança.30 é maior que 20, então 20 entra entre 10 e 30.
lista.inserir_ordenado(25) #Vai andando: 10 < 25 → vai pro 20 < 25 → vai pro 30 > 25.Então 25 entra entre 20 e 30.
lista.inserir_ordenado(5) #5 é menor que 10, então entra no início da lista.
lista.mostrar() #vai mostrar cada posição da lista, imprimindo:
        
            
        
        
   