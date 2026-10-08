catalogo = {}

while True:
    print("\n===Menu Catalogo===")
    print("1 - Adicionar Produtos")
    print("2 - Mostrar Produtos")
    print("=====================")
    opc = int(input("Digite uma Opção:"))

    if opc == 1:
        print("=======================================")
        print("Você selecionou para adicionar protudos")
        print("=======================================")
        codigo = int(input("Digite o Código do Produto: "))
        nome   = input("Digite o nome do Produto: ")      
        preco  = float(input("Digite o preço do Produto: "))  
        catalogo[codigo] = {"nome": nome, "preco": preco}
        print("Adicionado:",nome) 
    elif opc == 2:
        print("=======================================")
        print("Você selecionou para mostrar produtos")
        print("=======================================")
        for codigo in catalogo:
            print("Código do Produto",codigo)
            print("Nome do Produto:" ,catalogo[codigo]['nome'])     
            print("Preço do Produto:",catalogo[codigo]['preco'])  
            print("===========================================")
