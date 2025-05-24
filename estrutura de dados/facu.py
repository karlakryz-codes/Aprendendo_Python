from collections import deque
from typing import Deque

class Fila:
    
    def __init__(self):
       self.filaElementos: Deque[int] = deque()
        
    def incluirNaFila(self, elemento):

        self.filaElementos.append(elemento)  
        
    def incluirMuitosNaFila(self, variosElementos: list):

        for elemento in variosElementos:
            self.filaElementos.append(elemento)   
            
    def retirarDaFila(self):

        return self.filaElementos.popleft()
    
    def __str__(self):
    
     retorno = "\nEstrutura Fila (Frente para Trás)\n"
     for elemento in self.filaElementos:
         indice = self.filaElementos.index(elemento)
         retorno += str(indice) + " - " + str(elemento) + "\n"
     return retorno              

    
        
        
        
class Pilha: 
    
    def __init__(self):
        self.elementos = [] 
    
    def empilha(self, elemento):
        self.elementos.append(elemento)      

    def desempilha(self):
        return self.elementos.pop()

    def vazio(self):
        return len(self.elementos) == 0
    
    def __str__(self):
        retorno = "\nEstrutura Pilha (Topo para Base)\n"
        for elemento in self.elementos[::-1]:
            indice = self.elementos.index(elemento)
            retorno += str(indice) + " - " + str(elemento) + "\n"
        return retorno     
    
        

   

   

  
   
    

        

      