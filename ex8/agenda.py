# Programa para gerenciar uma agenda de shows.
# Carregar os eventos salvos em shows.json e permitir cadastrar novos shows.
# Criar funcionalidades para listar, buscar por cidade, vender ingressos
# e remover eventos.
# Validar datas, preços e quantidades de ingressos.
# Salvar as alterações no arquivo JSON para manter os dados
# mesmo depois que o programa for fechado.

import json
import os
from datetime import datetime


ARQUIVO = "shows.json"


def carregar_shows():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_shows(shows):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(shows, arquivo, ensure_ascii=False, indent=2)


def listar_shows(shows):
    if len(shows) == 0:
        print("Nenhum show cadastrado.")
        return

    shows_ordenados = sorted(
        shows,
        key=lambda show: datetime.strptime(show["data"], "%d/%m/%Y")
    )

    for i in range(len(shows_ordenados)):
        show = shows_ordenados[i]

        situacao = ""

        if show["ingressos"] == 0:
            situacao = "ESGOTADO"

        print(
            f'{i + 1}. {show["data"]} | {show["artista"]} | '
            f'{show["cidade"]} | R$ {show["preco"]:.2f} | '
            f'{show["ingressos"]} ingressos {situacao}'
            )
    return shows_ordenados    


def cadastrar_show(shows):
    artista = input("Artista/banda: ")
    cidade = input("Cidade: ")

    while True:
        texto_data = input("Data (dd/mm/aaaa): ")

        try:
            datetime.strptime(texto_data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    while True:
        try:
            preco = float(input("Preço do ingresso: R$ "))

            if preco > 0:
                break

            print("O preço deve ser maior que zero.")

        except ValueError:
            print("Digite um preço válido.")

    while True:
        try:
            ingressos = int(input("Ingressos disponíveis: "))

            if ingressos >= 0:
                break

            print("A quantidade não pode ser negativa.")

        except ValueError:
            print("Digite um número inteiro.")

    show = {
        "artista": artista,
        "cidade": cidade,
        "data": texto_data,
        "preco": preco,
        "ingressos": ingressos
    }

    shows.append(show)
    salvar_shows(shows)

    print("Show cadastrado e agenda salva.")


def shows_na_cidade(shows):
    cidade = input("Cidade: ").lower()

    encontrou = False

    for show in shows:
        if show["cidade"].lower() == cidade:
            print(show)
            encontrou = True

    if not encontrou:
        print("Nenhum show encontrado nessa cidade.")


def vender_ingressos(shows):
    if len(shows) == 0:
        print("Não existem shows cadastrados.")
        return

    shows_ordenados = listar_shows(shows)

    try:
        numero = int(input("Número do show: "))

        if numero < 1 or numero > len(shows):
            print("Número inválido.")
            return

        show = shows_ordenados[numero - 1]

        quantidade = int(input("Quantos ingressos? "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")

        elif quantidade > show["ingressos"]:
            print(f'Só restam {show["ingressos"]} ingressos.')

        else:
            show["ingressos"] -= quantidade
            valor = quantidade * show["preco"]

            salvar_shows(shows)

            print(
                f"Venda: {quantidade} x R$ {show['preco']:.2f} "
                f"= R$ {valor:.2f}"
            )

    except ValueError:
        print("Digite um número válido.")


def remover_show(shows):
    if len(shows) == 0:
        print("Não existem shows cadastrados.")
        return

    shows_ordenados = listar_shows(shows)

    try:
        numero = int(input("Número do show: "))

        if numero < 1 or numero > len(shows):
            print("Número inválido.")
            return

        removido = shows_ordenados[numero - 1]
        shows.remove(removido)

        salvar_shows(shows)

        print("Show de", removido["artista"], "removido.")

    except ValueError:
        print("Digite um número válido.")


shows = carregar_shows()
print(f"Agenda carregada: {len(shows)} shows.")

while True:
    print("\n===== AGENDA DE SHOWS =====")
    print("1 - Listar shows")
    print("2 - Cadastrar show")
    print("3 - Shows em uma cidade")
    print("4 - Vender ingressos")
    print("5 - Remover show")
    print("0 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        listar_shows(shows)

    elif escolha == "2":
        cadastrar_show(shows)

    elif escolha == "3":
        shows_na_cidade(shows)

    elif escolha == "4":
        vender_ingressos(shows)

    elif escolha == "5":
        remover_show(shows)

    elif escolha == "0":
        break

    else:
        print("Opção inválida.")