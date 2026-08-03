turma = {
    'Thomaz' : {'nota': 10. , 'frequencia': 80},
    'Felipe' : {'nota': 7. , 'frequencia': 45},
    'David '  : {'nota': 1.  , 'frequencia': 1000}
}

# Acesso aninhado

for aluno in turma:
    print(f"""
Nome: {aluno}
Nota: {turma[aluno]['nota']}
Frequencia: {turma[aluno]['frequencia']}
""")

# Percorrer e tomando decição

print("\tBoletim\n")
for nome, dados in turma.items():
    ok = dados['nota'] >= 7.0 and dados['frequencia'] >= 75
    print(f"{nome} : {"Aprovado" if ok else "Reprovado"}")