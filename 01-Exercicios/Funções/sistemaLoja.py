def produto():
    preco = float(input("Informe o preço do produto :"))
    quantidade = int(input("Quantidade de produtos :"))
    
    return quantidade, preco

def desconto(valor,percentual):
    valor_desconto = valor* (percentual/100)
    desconto_final = valor - valor_desconto
    return desconto_final,valor_desconto

def resumo(preco,quantidade,valor_total,forma_pagamento,valor_final,valor_desconto):
     print("*****************************************")
     print( "        Resumo Compra                   ")
     print(f"Preço unitário: R$ {preco:.2f}")
     print(f"Quantidade: {quantidade}")
     print(f"Valor total: R$ {valor_total:.2f}")
     if forma_pagamento == '1':
        pagamento = "À vista 💸"
     elif forma_pagamento == '2':
        pagamento = "Cartão Débito 💳"
     elif forma_pagamento == '3':
        pagamento = "Cartão Crédito 💳"
     else:
         pagamento = "Desconhecido ❓" 
         
     print(f"Forma de pagamento: {pagamento}")
     print(f"Desconto de R$: {valor_desconto}")
     print(f"Valor final: R$ {valor_final:.2f}")
     print("Obrigado pela compra! \U0001F60A")  
     print("******************************************")
     
       
    

qtd,preco = produto()
valor = qtd*preco


forma_pagamento = input("\nEscolha a forma de pagamento:\n1 - À Vista 💸\n2 - Cartão Débito 💳\n3 - Cartão Crédito 💳\nDigite o número: ")

if forma_pagamento in [ '1','2'] :
    percentual = float(input("Informe o percentual de desconto (%): "))
    valor_final, valor_desconto = desconto(valor, percentual)
    
elif forma_pagamento == '3':
    valor_final= valor
    valor_desconto = 0
    

else:
    print("Opção inválida. Será considerado sem desconto.")
    valor_final = valor
    valor_desconto = 0
           
resumo(preco, qtd, valor, forma_pagamento, valor_final,valor_desconto)












    



 