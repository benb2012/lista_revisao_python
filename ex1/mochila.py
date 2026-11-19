# Programa para montar uma mochila de camping.
# Deve receber os nomes e pesos dos itens até o usuário digitar "FIM".
# Ao final, mostrar um resumo com quantidade, peso total, média,
# item mais pesado e quanto ultrapassou ou ainda cabe no limite de 15 kg.
# Validar os pesos digitados para evitar valores inválidos.

print("=== MOCHILA DE CAMPING ===")
print("Digite os itens. Para terminar, digite FIM.")

item = ""
mochila = []
pesomax = 15
pesoatuul = 0
while True:
    
    item = input("Item: ")
    if item.lower() == "fim":
        break

    try:
        peso = input("Peso (kg): ").replace(",", ".")
        peso = float(peso)
        if peso <= 0:
            print("O peso precisa ser um número positivo (maior que zero).")
            continue

        pesoatuul+=peso
        if pesoatuul > pesomax:
            print("Atenção")

        coisa = {"item": item,
                 "peso": peso}
        mochila.append(coisa)

    except ValueError:
        print("O valor precisa ser um numero   ")
        

        
