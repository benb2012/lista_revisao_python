# Programa para calcular os custos e a organização de uma excursão escolar.
# Receber a quantidade de turmas, seus nomes e o número de alunos inscritos.
# Calcular a quantidade de professores acompanhantes (1 para cada 15 alunos),
# o número de ônibus necessários, lugares sobrando e custo por aluno.
# Ao final, mostrar um resumo e identificar a turma com mais inscritos.
#

alunos_totais = 0

while True:
    turmas = float(input("Quantas turmas vão participar? "))

    if turmas % 1 != 0:
        print("O número de turmas deve ser inteiro.")
    elif turmas <= 0:
        print("O número de turmas deve ser maior que zero.")
    else:
        turmas = int(turmas)
        break

nome_maior_turma = ""
maior_quantidade = 0

for i in range(turmas):
    nome_turma = input("Nome da turma: ")

    while True:
        inscritos = float(input("Número de inscritos: "))

        if inscritos % 1 != 0:
            print("O número de inscritos deve ser inteiro.")
        elif inscritos <= 0:
            print("O número de inscritos deve ser maior que zero.")
        else:
            inscritos = int(inscritos)
            break

    alunos_totais += inscritos

    if inscritos > maior_quantidade:
        maior_quantidade = inscritos
        nome_maior_turma = nome_turma

professores = alunos_totais // 15

if alunos_totais % 15 > 0:
    professores += 1

total_pessoas = alunos_totais + professores

onibus = total_pessoas // 44

if total_pessoas % 44 > 0:
    onibus += 1

lugares_sobrando = (onibus * 44) - total_pessoas

custo_total = onibus * 1800

valor_por_aluno = custo_total / alunos_totais

print("Total de alunos:", alunos_totais)
print("Total de professores:", professores)
print("Total de pessoas:", total_pessoas)
print("Número de ônibus:", onibus)
print("Lugares sobrando:", lugares_sobrando)
print("Custo total: R$", custo_total)
print(f"Valor por aluno: R$ {valor_por_aluno:.2f}")
print(f"Turma com mais inscritos: {nome_maior_turma} ({maior_quantidade} alunos)")
