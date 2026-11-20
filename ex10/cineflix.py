# Programa principal da plataforma Cineflix.
# Importar as funções de banco_streaming.py e tempo.py.
# Permitir que diferentes perfis consultem o catálogo e registrem
# os títulos assistidos, informando a quantidade de minutos.
# Criar funcionalidades para visualizar o histórico, consultar os mais
# assistidos e comparar o tempo assistido por perfil.
# Permitir exportar um relatório em formato JSON.
# Criar um menu que continue funcionando até o usuário escolher sair.


import json
from datetime import date
import banco_streaming
import tempo


conn = banco_streaming.conectar()

perfil = input("Nome do perfil: ")

while True:
    print(f"\n===== CINEFLIX ({perfil}) =====")
    print("1 - Ver catálogo")
    print("2 - Registrar que assisti")
    print("3 - Meu histórico")
    print("4 - Mais assistidos")
    print("5 - Tempo assistido por perfil")
    print("6 - Exportar relatório JSON")
    print("7 - Trocar de perfil")
    print("0 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        titulos = banco_streaming.listar_titulos(conn)

        for item in titulos:
            id, titulo, tipo, genero, ano, duracao, classificacao, nota = item

            print(
                f"{id} - {titulo} | {tipo} | {genero} | "
                f"{ano} | {classificacao} | nota {nota}"
            )

    elif escolha == "2":
        try:
            titulo_id = int(input("Id do título: "))
            minutos = int(input("Quantos minutos você assistiu? "))

            if minutos <= 0:
                print("Os minutos devem ser maiores que zero.")

            else:
                data_atual = date.today().isoformat()

                registrado = banco_streaming.registrar_visualizacao(
                    conn, perfil, titulo_id, minutos, data_atual
                )

                if registrado:
                    print("Registrado!")
                else:
                    print("Não existe título com esse id.")

        except ValueError:
            print("Digite números inteiros.")

    elif escolha == "3":
        registros = banco_streaming.historico(conn, perfil)

        total = 0

        for registro in registros:
            data, titulo, minutos = registro
            total += minutos

            print(data, titulo, tempo.formatar_duracao(minutos))

        print(
            f"Total: {tempo.formatar_duracao(total)} "
            f"em {len(registros)} sessões"
        )

    elif escolha == "4":
        registros = banco_streaming.mais_assistidos(conn)

        if len(registros) == 0:
            print("Ainda não existem visualizações.")

        for i in range(len(registros)):
            titulo, quantidade = registros[i]
            print(f"{i + 1}º {titulo} - {quantidade} vez(es)")

    elif escolha == "5":
        registros = banco_streaming.tempo_por_perfil(conn)

        for registro in registros:
            nome, minutos = registro
            print(nome, tempo.formatar_duracao(minutos))

    elif escolha == "6":
        mais_assistidos = banco_streaming.mais_assistidos(conn)
        tempos = banco_streaming.tempo_por_perfil(conn)

        relatorio = {
            "data": date.today().isoformat(),
            "mais_assistidos": [],
            "tempo_por_perfil": []
        }

        for registro in mais_assistidos:
            titulo, quantidade = registro

            relatorio["mais_assistidos"].append({
                "titulo": titulo,
                "visualizacoes": quantidade
            })

        for registro in tempos:
            nome, minutos = registro

            relatorio["tempo_por_perfil"].append({
                "perfil": nome,
                "minutos": minutos
            })

        with open("relatorio.json", "w", encoding="utf-8") as arquivo:
            json.dump(relatorio, arquivo, ensure_ascii=False, indent=2)

        print("Relatório JSON gravado.")

    elif escolha == "7":
        perfil = input("Nome do novo perfil: ")

    elif escolha == "0":
        break

    else:
        print("Opção inválida.")


conn.close()