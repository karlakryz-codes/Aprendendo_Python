pessoas = []

# Coletando os dados
for i in range(5):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas.append((nome, idade))

print("\n" + "=" * 40)  #caractere "=" vai se repetir 40 vezes 
print("📋 Lista de todas as pessoas cadastradas:")
print("-" * 40)
for nome, idade in pessoas:
    print(f"👤 Nome: {nome:<10} | 🎂 Idade: {idade} anos") #significa que o texto do nome será alinhado à esquerda e vai ocupar 10 espaços na linha.
print("=" * 40)

# Calculando a média das idades
media_idade = sum(idade for nome, idade in pessoas) / len(pessoas)

print("\n" + "=" * 40)
print(f"📊 A média das idades é: {media_idade:.2f} anos")
print("=" * 40)

# Pessoas com idade acima da média
print("🚀 Pessoas com idade acima da média:")
print("-" * 40)
encontrou = False  #Variável booleana usada para marcar se pelo menos uma pessoa com idade acima da média foi encontrada.
for nome, idade in pessoas:
    if idade > media_idade:
        print(f"👉 Nome: {nome:<10} | Idade: {idade} anos")
        encontrou = True
if not encontrou:
    print("Nenhuma pessoa acima da média.")

print("=" * 40)

# Descobrindo mais velho e mais novo
mais_velho = max(pessoas, key=lambda p: p[1])
mais_novo = min(pessoas, key=lambda p: p[1])

print(f"👴 A pessoa mais velha é {mais_velho[0]} com {mais_velho[1]} anos.")
print(f"🧒 A pessoa mais nova é {mais_novo[0]} com {mais_novo[1]} anos.")
print("=" * 40)
