# Programa de gerenciamento e consulta do catálogo da Cineflix.
# Carregar os títulos armazenados no arquivo catalogo.json.
# Criar funções para listar, filtrar por gênero, buscar títulos,
# verificar classificação etária, ordenar por nota e gerar estatísticas.
# Criar um menu que permita acessar todas essas funcionalidades.
# Os dados devem ser lidos do JSON, sem precisar cadastrar os títulos manualmente.





import json

with open("ex7/catalogo.json", "r", encoding="utf-8") as arquivo:
    titulos = json.load(arquivo)

print(f"Titulos carregados:{len(titulos)}")

while True:
    print("(1)- Listar todas as informações dos títulos\n(2)- Filtrar por gênero\n(3)- Buscar Título\n(4)- Títulos para a minha idade\n(5)- Mais bem avaliados\n(6)- Estatísticas\n(0)- Sair")
    

    opcao = input("-> ")

    if opcao == "1":

        print(f"| {'ID':<4} | {'Título':<25} | {'Tipo':<12} | {'Gênero':<15} | {'Ano':<6} | {'Duração':<10} | {'Classificação':<15} | {'Nota':<5} |")

        for i in titulos:
            print(f"| {i['id']:<4} | {i['titulo']:<25} | {i['tipo']:<12} | {i['genero']:<15} | {i['ano']:<6} | {i['duracao_min']:<10} | {i['classificacao']:<15} | {i['nota']:<5} |")

    if opcao == "2":
        generos = []

        for i in titulos:
            if i['genero'] not in generos:
                generos.append(i['genero'])
        
        generos.sort()

        print("Gêneros disponiveis:")
        for i in generos:
            print(f"| {i :<15} |")

        gescolha = input("Escolha um Gênero: ").lower()

        print(f"| {'ID':<4} | {'Título':<25} | {'Tipo':<12} | {'Gênero':<15} | {'Ano':<6} | {'Duração':<10} | {'Classificação':<15} | {'Nota':<5} |")
        for i in titulos:
            if gescolha == (i['genero'].lower()):
                print(f"| {i['id']:<4} | {i['titulo']:<25} | {i['tipo']:<12} | {i['genero']:<15} | {i['ano']:<6} | {i['duracao_min']:<10} | {i['classificacao']:<15} | {i['nota']:<5} |")

    if opcao == "3":
        
        
        trecho = input("Digite o título desejado: ")

        print(f"| {'ID':<4} | {'Título':<25} | {'Tipo':<12} | {'Gênero':<15} | {'Ano':<6} | {'Duração':<10} | {'Classificação':<15} | {'Nota':<5} |")
        for i in titulos:
            if trecho.lower() in i['titulo'].lower():
                print(f"| {i['id']:<4} | {i['titulo']:<25} | {i['tipo']:<12} | {i['genero']:<15} | {i['ano']:<6} | {i['duracao_min']:<10} | {i['classificacao']:<15} | {i['nota']:<5} |")
                

    if opcao == "4":

        idade = input("Digite sua idade: ")
        if idade.lower() == "l":
            idade = 0
        else:
            idade = int(idade)

        

        
        print(f"| {'ID':<4} | {'Título':<25} | {'Tipo':<12} | {'Gênero':<15} | {'Ano':<6} | {'Duração':<10} | {'Classificação':<15} | {'Nota':<5} |")

        for i in titulos:
            if idade>= i['classificacao']:
                print(f"| {i['id']:<4} | {i['titulo']:<25} | {i['tipo']:<12} | {i['genero']:<15} | {i['ano']:<6} | {i['duracao_min']:<10} | {i['classificacao']:<15} | {i['nota']:<5} |")

    if opcao == "5":
        quantidade = (input("Quantos titulos deseja mostrar? (Padrão = 5) : "))

        if quantidade == "":
            quantidade = 5
        else: 
            quantidade = int(quantidade)

        tituldiscard = titulos
        teste = {"id": 0,
    "titulo": "x",
    "tipo": "x",
    "genero": "x",
    "ano": 0,
    "duracao_min": 0,
    "classificacao": 0,
    "nota": 0}

        print(f"| {'ID':<4} | {'Título':<25} | {'Tipo':<12} | {'Gênero':<15} | {'Ano':<6} | {'Duração':<10} | {'Classificação':<15} | {'Nota':<5} |")
        for x in range(quantidade):
            for i in tituldiscard:
                if i['nota'] > teste['nota']:
                    teste = i

            tituldiscard.remove(teste)
            print(f"| {teste['id']:<4} | {teste['titulo']:<25} | {teste['tipo']:<12} | {teste['genero']:<15} | {teste['ano']:<6} | {teste['duracao_min']:<10} | {teste['classificacao']:<15} | {teste['nota']:<5} |")
            
            teste = {"id": 0,
                "titulo": "x",
                "tipo": "x",
                "genero": "x",
                "ano": 0,
                "duracao_min": 0,
                "classificacao": 0,
                "nota": 0}
        
    if opcao == "6":
        print("Estatisticas:")

        print(f"Titulos carregados:{len(titulos)}")

        contf = 0
        conts = 0

        for i in titulos:
            if i["tipo"].lower() == "filme".lower():
                contf +=1
            else:
                conts +=1
        print(f"Numero de Filmes: {contf}")
        print(f"Numero de Séries: {conts}")

        somanotas = 0
        for i in titulos:
            somanotas += i['nota']
        media = somanotas / len(titulos)
        
        print(f"Media geral dos titulos (Arredondada): {round(media, 1)}")

        generos = []
        for i in titulos:
            if i['genero'] not in generos:
                generos.append(i['genero'])
                
                generos.sort()
        
        print("\nGêneros disponiveis:")
        for i in generos:
            print(f"| {i :<15} |")


    if opcao == "0":
        print("Tenha um bom dia")
        break