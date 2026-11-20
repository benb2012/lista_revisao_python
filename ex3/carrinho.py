# Programa que simula o carrinho de compras de uma loja virtual.
# Criar funções para calcular o subtotal dos itens, aplicar cupons,
# calcular o frete e determinar o valor das parcelas.
# Receber produtos até o usuário deixar o nome vazio.
# Ao final, calcular descontos, frete e apresentar a nota da compra.
# As funções de cálculo devem utilizar parâmetros e return, sem print.
#













def subtotal_item(preco, quantidade=1):
    return preco * quantidade


def aplicar_cupom(total, cupom):
    cupom = cupom.upper().replace(" ", "")

    if cupom == "PROMO10":
        novo_valor = total - (total * 0.10)
        return novo_valor, 10

    elif cupom == "VOLTASAULAS":
        novo_valor = total - (total * 0.15)
        return novo_valor, 15

    elif cupom == "BLACK25":
        novo_valor = total - (total * 0.25)
        return novo_valor, 25

    else:
        novo_valor = total
        return novo_valor, 0


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0.0
    else:
        return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    else:
        return (total * (1 + 0.02 * parcelas)) / parcelas









carrinho = 0

while True:
    produto = input("Produto (Enter para fechar o carrinho): ")

    if produto == "":
        break

    preco = float(input("Preço: R$ "))

    while preco <= 0:
        print("Digite um valor maior que zero.")
        preco = float(input("Preço: R$ "))

    while True:
        quantidade = float(input("Quantidade: "))

        if quantidade % 1 != 0:
            print("Digite uma quantidade inteira.")
        elif quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
        else:
            quantidade = int(quantidade)
            break

    subtotal = subtotal_item(preco, quantidade)
    carrinho += subtotal

    print(f"{quantidade} x {produto} = R$ {subtotal:.2f} (carrinho: R$ {carrinho:.2f})")


cupom = input("Cupom de desconto (Enter se não tiver): ").upper()

novo_total, percentual = aplicar_cupom(carrinho, cupom)

desconto = carrinho - novo_total

frete = calcular_frete(novo_total)

total = novo_total + frete

while True:
    parcelas = int(input("Em quantas parcelas (1 a 12)? "))

    if parcelas < 1 or parcelas > 12:
        print("Escolha entre 1 e 12 parcelas.")
    else:
        break

valor_por_parcela = valor_parcela(total, parcelas)

print("\n=== NOTA ===")
print(f"Subtotal: R$ {carrinho:.2f}")
print(f"Desconto: {percentual}% (R$ {desconto:.2f})")
print(f"Frete: R$ {frete:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Pagamento: {parcelas} x R$ {valor_por_parcela:.2f}")
