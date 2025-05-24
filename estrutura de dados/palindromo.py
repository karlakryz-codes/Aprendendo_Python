def palindromo(palavra):
   if palavra.lower() == palavra.lower()[::-1]:
     return f"A palavra {palavra} é um Palíndromo"
   else:
     return f"A palavra {palavra} não é um Palíndromo" 
 
palavra = input("Informe a palavra: ")  
     
resultado =palindromo(palavra)
print(resultado)
    
    