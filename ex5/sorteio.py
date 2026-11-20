# Programa de sorteio de brindes da Feira de Ciências.
# Importar e utilizar as funções do módulo utilidades.py.
# Receber os nomes dos participantes, impedindo nomes repetidos.
# Receber os brindes e sortear ganhadores sem repetir participantes.
# Utilizar random e datetime para realizar o sorteio e registrar data e hora.
# Não utilizar input() diretamente neste arquivo.

import random
import datetime
import utilidades


print("=== SORTEIO DE BRINDES - FEIRA DE CIÊNCIAS ===")

participantes = []

print("Digite os nomes dos participantes.")
print("Deixe vazio para terminar.")

while True:
    nome = utilidades.ler_texto("Participante: ", vazio=True)

    if nome == "":
        break

    nome_repetido = False

    for participante in participantes:
        if participante.lower() == nome.lower():
            nome_repetido = True
            break

    if nome_repetido:
        print("Esse nome já está na lista.")
    else:
        participantes.append(nome)


if len(participantes) == 0:
    print("Nenhum participante cadastrado.")

else:
    quantidade = utilidades.ler_inteiro(
        "Quantos brindes serão sorteados? ",
        1,
        len(participantes)
    )

    brindes = []

    for i in range(quantidade):
        brinde = utilidades.ler_texto(f"Brinde {i + 1}: ")
        brindes.append(brinde)

    ganhadores = random.sample(participantes, quantidade)

    print(utilidades.linha("="))

    data = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")
    print("Sorteio realizado em", data)
    print(f"{len(participantes)} participantes, {quantidade} brindes")

    print(utilidades.linha("="))

    for i in range(quantidade):
        print(brindes[i], "->", ganhadores[i])