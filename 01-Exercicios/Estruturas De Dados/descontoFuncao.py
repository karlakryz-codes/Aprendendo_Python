
def calcula_desconto(preco,percentual_desconto):
   desconto= preco * (percentual_desconto/100)
   preco_final = preco - desconto
   return preco_final
   
   
preco= float(input("Digite o preço do produto: R$ ")) 
percentual_desconto = float(input("Qual taxa de desconto (%):"))


preco_com_desconto = calcula_desconto(preco,percentual_desconto)
print(f"O preço com  {percentual_desconto:.0f}%  de desconto é: R$ {preco_com_desconto:.2f}")

