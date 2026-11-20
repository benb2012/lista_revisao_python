# Programa para calcular quanto tempo será necessário para assistir a uma série.
# Criar funções para formatar durações, somar tempos, calcular dias necessários
# para terminar a série e classificar a maratona como Leve, Média ou Intensa.
# Receber a quantidade de temporadas, episódios e duração média dos episódios.
# Mostrar o tempo de cada temporada e o tempo total da série.


def formatar_duracao_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60

    if horas == 0:
        return f"{minutos_restantes:02d}min"
    else:
        return f"{horas}h {minutos_restantes:02d}min"


def tempo_total(duracoes):
    total = 0

    for i in duracoes:
        total += i

    return total


def dias_para_terminar(total_minutos, minutos_por_dia):
    dias = total_minutos // minutos_por_dia

    if total_minutos % minutos_por_dia > 0:
        dias += 1

    return dias


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    else:
        return "Intensa"


print("=== MARATONA DE SÉRIES ===")

nome_serie = input("Nome da série: ")

while True:
    temporadas = float(input("Quantidade de temporadas: "))

    if temporadas % 1 != 0:
        print("Digite um número inteiro.")
    elif temporadas <= 0:
        print("A quantidade deve ser maior que zero.")
    else:
        temporadas = int(temporadas)
        break

duracoes = []

for i in range(temporadas):
    print(f"\nTemporada {i + 1}")

    while True:
        episodios = float(input("Número de episódios: "))

        if episodios % 1 != 0:
            print("Digite um número inteiro.")
        elif episodios <= 0:
            print("A quantidade deve ser maior que zero.")
        else:
            episodios = int(episodios)
            break

    while True:
        duracao = float(input("Duração média do episódio (minutos): "))

        if duracao % 1 != 0:
            print("Digite um número inteiro.")
        elif duracao <= 0:
            print("A duração deve ser maior que zero.")
        else:
            duracao = int(duracao)
            break

    minutos_temporada = episodios * duracao

    duracoes.append(minutos_temporada)


print(f"\n=== {nome_serie.upper()} ===")

for i in range(temporadas):
    print(f"Temporada {i + 1}: {formatar_duracao_minutos(duracoes[i])}")


total_minutos = tempo_total(duracoes)

print(f"Tempo total: {formatar_duracao_minutos(total_minutos)}")
print(f"Classificação: {classificar_maratona(total_minutos)}")


while True:
    minutos_dia = float(input("\nQuantos minutos por dia você pode assistir? "))

    if minutos_dia % 1 != 0:
        print("Digite um número inteiro.")
    elif minutos_dia <= 0:
        print("O tempo deve ser maior que zero.")
    else:
        minutos_dia = int(minutos_dia)
        break


dias = dias_para_terminar(total_minutos, minutos_dia)
dias_padrao = dias_para_terminar(total_minutos, 120)

print(f"\nTempo solicitado: {dias} dias")
print(f"Tempo padrão (120 min/dia): {dias_padrao} dias")

