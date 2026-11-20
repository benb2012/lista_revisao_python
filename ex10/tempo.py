# Módulo responsável pela formatação de durações.
# Reaproveitar a função formatar_duracao() desenvolvida na questão 4.
# Ela deverá transformar uma quantidade de minutos em um texto legível,
# como "2h05min" ou "45min".
# Este módulo será utilizado pelo programa cineflix.py.


def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60

    if horas > 0:
        return f"{horas}h{resto:02d}min"
    else:
        return f"{resto}min"