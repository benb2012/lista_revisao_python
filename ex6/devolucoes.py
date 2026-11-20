# Programa para controlar as devoluções de livros da biblioteca.
# Importar as funções do módulo multas.py.
# Receber o título dos livros e as datas previstas e reais de devolução.
# Permitir que o usuário deixe a data de devolução vazia para utilizar a data atual.
# Mostrar os dias de atraso e a multa de cada livro.
# Ao final, apresentar a quantidade de livros devolvidos,
# quantos tiveram atraso e o total arrecadado em multas.    


from datetime import date
import multas


print("=== BALCÃO DE DEVOLUÇÕES ===")

livros_devolvidos = 0
livros_atrasados = 0
total_multas = 0

while True:
    titulo = input("\nTítulo do livro (Enter para encerrar): ")

    if titulo == "":
        break

    while True:
        texto_prevista = input("Data prevista (dd/mm/aaaa): ")

        try:
            data_prevista = multas.converter_data(texto_prevista)
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    while True:
        texto_devolucao = input("Data da devolução (Enter = hoje): ")

        if texto_devolucao == "":
            data_devolucao = date.today()
            break

        try:
            data_devolucao = multas.converter_data(texto_devolucao)
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    dias = multas.dias_de_atraso(data_prevista, data_devolucao)
    multa = multas.valor_multa(dias)

    livros_devolvidos += 1
    total_multas += multa

    if dias > 0:
        livros_atrasados += 1
        print(f"'{titulo}' com {dias} dia(s) de atraso. Multa: R$ {multa:.2f}")
    else:
        print(f"'{titulo}' devolvido no prazo. Obrigado!")


print("\n=== FECHAMENTO DO DIA ===")
print("Livros devolvidos:", livros_devolvidos)
print("Com atraso:", livros_atrasados)
print(f"Total em multas: R$ {total_multas:.2f}")