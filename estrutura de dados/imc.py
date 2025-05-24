def calcular_imc(peso,altura):
    return peso/(altura*altura)

def classificar_imc(imc):    
  if imc < 16:
   return "Magreza grave"
  elif imc >= 16 and imc < 17:
       return "Magreza moderada"
  elif imc >= 17 and imc < 18.5:
       return "Magreza leve"
  elif imc >= 18.5 and imc < 25:
       return "Peso normal"
  elif imc >= 25 and imc < 30:
       return "Sobrepeso"
  elif imc >= 30 and imc < 35:
       return "Obesidade grau I"
  elif imc >= 35 and imc < 40:
       return "Obesidade grau II"
  else:
      return "Obesidade grau III"
  
  
altura = float(input("Informe a altura (m) \U0001F4CF: "))  
peso = float(input("Informe o peso em (Kg) \U00002696 : "))


imc=calcular_imc(peso,altura) 
classificacao = classificar_imc(imc) 


print("|" * 35)
print("|" + "IMC CALCULADO \U0001F9CD".center(32) + "|")
print("|" * 35)
print("| " + f"Seu IMC é: {imc:.2f}".ljust(32) + "|")
print("| " + f"Classificação: {classificacao}".ljust(32) + "|")
print("|" * 35)

    
    

    
    
    

                
         
          
    
    
    
    






    
    
    
    

    
    
    
