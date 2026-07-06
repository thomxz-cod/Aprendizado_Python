numCadastros = int(input("Quantos alunos serão cadastrados: "))

listaAlunos = []

for i in range(numCadastros):
    aluno = []
    nomeAluno = input("\nDigite o nome do aluno: ")
    primeiraNota = float(input("Digite a nota do primeiro bimestre: "))
    segundaNota = float(input("Digite a nota do segundo bimestre: "))
    media = round((primeiraNota + segundaNota) / 2, 2)
    
    aluno.append(nomeAluno)
    aluno.append(media)

    listaAlunos.append(aluno)

print("\n===== RELATÓRIO =====\n")

totalNotas = [] 
for aluno in listaAlunos:
    if aluno[1] >= 7:
        situacao = "Aprovado"
    elif aluno[1] >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    totalNotas.append(situacao)

    print(f"Aluno: {aluno[0]}")
    print(f"Média: {aluno[1]}")
    print(f"Situação: {situacao}\n")

print("======= TOTAL =======\n")

contAprov = 0
contRecup = 0
contRepro = 0
for nota in totalNotas:
    if nota == "Aprovado":
        contAprov += 1
    elif nota == "Recuperação":
        contRecup += 1
    elif nota == "Reprovado":
        contRepro += 1

print(f"""Aprovados: {contAprov}
Recuperação: {contRecup}
Reprovados: {contRepro}
""")

print("=== FIM RELATÓRIO ===\n")
