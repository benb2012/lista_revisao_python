# Programa principal para controlar o estoque de uma loja de camping.
# Importar as funções do módulo banco_estoque.py.
# Criar um menu para cadastrar, listar e buscar produtos,
# registrar entradas e saídas, verificar produtos para reposição
# e consultar o valor total do estoque.
# O menu deve continuar funcionando até o usuário escolher sair.


import banco_estoque


def mostrar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto encontrado.")
        return

    print("ID | Produto | Categoria | Preço | Qtd")

    for produto in produtos:
        id, nome, categoria, preco, quantidade, minimo = produto

        aviso = ""

        if quantidade < minimo:
            aviso = "<- repor"

        print(
            f"{id} | {nome} | {categoria} | "
            f"R$ {preco:.2f} | {quantidade} {aviso}"
        )


conn = banco_estoque.conectar()

while True:
    print("\n===== ESTOQUE - LOJA DE CAMPING =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar por nome")
    print("4 - Entrada (chegou mercadoria)")
    print("5 - Saída (venda)")
    print("6 - Produtos para repor")
    print("7 - Valor total do estoque")
    print("0 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        nome = input("Nome: ")
        categoria = input("Categoria: ")

        try:
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade inicial: "))
            minimo = int(input("Estoque mínimo: "))

            if preco <= 0 or quantidade < 0 or minimo < 0:
                print("Valores inválidos.")
            else:
                id = banco_estoque.cadastrar(
                    conn, nome, categoria, preco, quantidade, minimo
                )

                print("Produto cadastrado. ID:", id)

        except ValueError:
            print("Digite valores numéricos válidos.")

    elif escolha == "2":
        mostrar_produtos(banco_estoque.listar(conn))

    elif escolha == "3":
        texto = input("Parte do nome: ")
        mostrar_produtos(banco_estoque.buscar(conn, texto))

    elif escolha == "4":
        try:
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade que chegou: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            elif banco_estoque.entrada(conn, id, quantidade):
                print("Entrada registrada.")
            else:
                print("Produto não encontrado.")

        except ValueError:
            print("Digite números inteiros.")

    elif escolha == "5":
        try:
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade vendida: "))

            print(banco_estoque.saida(conn, id, quantidade))

        except ValueError:
            print("Digite números inteiros.")

    elif escolha == "6":
        mostrar_produtos(banco_estoque.estoque_baixo(conn))

    elif escolha == "7":
        total = banco_estoque.valor_total(conn)
        print(f"Valor total em estoque: R$ {total:.2f}")

    elif escolha == "0":
        break

    else:
        print("Opção inválida.")


conn.close()