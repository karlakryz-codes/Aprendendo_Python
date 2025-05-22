VetIdade =[]

for x in range(8):
    idade = int(input(f"Idade {x+1}:"))
    VetIdade.append(idade)
    
media = sum(VetIdade) /len(VetIdade) 

idade_acima = sum(1 for idade in VetIdade if idade > media) 

print("\n============================")
print(f"Média das idades: {media:.2f}")
print(f"Número de idades acima da média: {idade_acima}")

print("Idades acima da média são:")
for idade in VetIdade:
    if idade > media:
        print(idade)


print(f"A maior idade é: {max(VetIdade)}")
print(f"A menor idade é: {min(VetIdade)}")

print("============================")










