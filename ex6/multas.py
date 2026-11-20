# Módulo responsável pelas regras de cálculo das multas da biblioteca.
# Criar converter_data() para transformar textos em datas.
# Criar dias_de_atraso() para calcular quantos dias o livro foi devolvido atrasado.
# Criar valor_multa() para calcular a multa de R$ 1,50 por dia,
# respeitando o limite máximo de R$ 30,00.
# Incluir testes das funções usando if __name__ == "__main__".
# Este módulo será utilizado pelo arquivo devolucoes.py.

from datetime import datetime


def converter_data(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


def dias_de_atraso(data_prevista, data_devolucao):
    dias = (data_devolucao - data_prevista).days

    if dias < 0:
        return 0

    return dias


def valor_multa(dias, por_dia=1.50, maximo=30.00):
    multa = dias * por_dia

    if multa > maximo:
        multa = maximo

    return multa


if __name__ == "__main__":
    prevista = converter_data("05/11/2026")
    devolucao = converter_data("10/11/2026")

    dias = dias_de_atraso(prevista, devolucao)

    print("Dias de atraso:", dias)
    print("Multa: R$", valor_multa(dias))