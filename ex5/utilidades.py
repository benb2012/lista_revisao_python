# Módulo de funções auxiliares para leitura e formatação.
# Criar ler_texto() para receber textos e validar campos vazios.
# Criar ler_inteiro() para receber números inteiros e conferir limites.
# Criar linha() para gerar linhas de separação.
# Incluir um bloco if __name__ == "__main__" para testar as funções.
# Este módulo será utilizado pelo arquivo sorteio.py.


def ler_texto(mensagem, vazio=False):
    while True:
        texto = input(mensagem).strip()

        if texto != "" or vazio:
            return texto

        print("Digite alguma coisa.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo is not None and numero < minimo:
                print(f"O valor mínimo é {minimo}.")
            elif maximo is not None and numero > maximo:
                print(f"O valor máximo é {maximo}.")
            else:
                return numero

        except ValueError:
            print("Digite um número inteiro.")


def linha(caractere="-", tamanho=40):
    return caractere * tamanho


if __name__ == "__main__":
    print(ler_texto("Nome: "))
    print(ler_inteiro("Idade: ", 1, 100))
    print(linha("=" , 5))