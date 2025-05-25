# Criamos uma lista vazia para armazenar todos os produtos cadastrados
produtos = []

# Início de um laço que vai se repetir até o usuário decidir parar
while True:
    # Criamos um dicionário para armazenar os dados de um único produto
    produto = {
        "codigo": 0,
        "descricao": "",
        "preco": 0.0,
        "quantidade": 0
    }

    # Coletamos os dados do produto com input do usuário
    produto["codigo"] = int(input("Digite o código do produto:\n"))
    produto["descricao"] = input("Digite a descrição do produto:\n")
    produto["preco"] = float(input("Digite o preço do produto:\n"))
    produto["quantidade"] = int(input("Digite a quantidade em estoque do produto:\n"))

    # Adicionamos o dicionário (produto) à lista de produtos
    produtos.append(produto)

    # Mostramos os dados do produto cadastrado
    print("\n📦 Dados do produto cadastrado:")
    print("Código:", produto["codigo"])
    print("Descrição:", produto["descricao"])
    print("Preço: R$", produto["preco"])
    print("Quantidade em estoque:", produto["quantidade"])

    # Perguntamos se o usuário deseja cadastrar outro produto
    continuar = input("\nDeseja cadastrar outro produto? (s/n): ").lower()

    # Se a resposta não for "s", o programa sai do laço com break
    if continuar != "s":
        print("\nCadastro finalizado. Produtos cadastrados:")
        break  # Encerra o loop

# Após sair do loop, mostramos todos os produtos cadastrados
for i, p in enumerate(produtos):
    print(f"\nProduto {i+1}:")
    print("Código:", p["codigo"])
    print("Descrição:", p["descricao"])
    print("Preço: R$", p["preco"])
    print("Quantidade em estoque:", p["quantidade"])
