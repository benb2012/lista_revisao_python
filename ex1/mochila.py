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
passou = False

maisor = {"item": "x",
            "peso": 0}




while True:
    
    item = input("\nItem: ")
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
            print(f"Atenção: a mochila já tem {(pesoatuul):.2f} kg (limite 15 kg)!")
            passou = True

        coisa = {"item": item,
                 "peso": peso}

        if coisa["peso"]> maisor['peso']:
            maisor = coisa
        
        mochila.append(coisa)




    except ValueError:
        print("O valor precisa ser um numero   ")

print("===RESUMO===")
for indice, i in enumerate(mochila):
    print(f"| {indice+1:<4} | {i["item"]:<15} | {i["peso"]:<4} kg")

print(f"Items: {len(mochila)}")
print(f"Peso total: {pesoatuul:.2f} kg")
print(f"Peso medio: {(pesoatuul/len(mochila)):.2f} kg")
print(f"Item mais pesado: {maisor['item']} ({maisor['peso']} kg)")

if passou:
    print(f"Tire {(pesoatuul - 15.0):.2f} kg da mochila para ficar dentro do limite")
else:
    print(f"Espaço restante: {(15.0 - pesoatuul):.2f} kg (de 15 kg)")


        

        
