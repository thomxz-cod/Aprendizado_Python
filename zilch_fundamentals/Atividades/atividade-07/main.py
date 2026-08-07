media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno (0 a 1): "))
if frequencia >= 0.75 and media >= 7.0:
    print("Aprovado.")
elif frequencia < 0.75:
    print("Reprovado por frequência.")
else:
    print("Reprovado por média.")