catalogo = {}

while True:
    print("\n===Menu Catalogo===")
    print("1 - Adicionar Produtos")
    opc = int(input("Digite uma Opção:"))

    if opc == 1:
        print("=======================================")
        print("Você selecionou para adicionar protudos")
        print("=======================================")
        catalogo["codigo"] = int(input("Digite o Código do Produto:"))
        catalogo["nome"] = input("Digite o nome do Produto:")
        catalogo["preco"] = float(input("Digite o preço do Produto:"))
        print("Produto Adicionado com Sucesso")
    elif opc == 2:
        print("=======================================")
        print("Você selecionou para mostrar produtos")
        print("=======================================")
        print("Código:",catalogo["codigo"])

