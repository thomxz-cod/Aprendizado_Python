""" Sintaxe:
"chave" : "valor"
"""

# Primeira maneira de criar dicionario 
aluno = {} # vazio
aluno["nome"] = "Thomaz"
aluno["idade"] = 18
aluno["nota"] = 10

print(aluno)
print(f"""\nAluno:\n
Nome: {aluno["nome"]}
Idade: {aluno["idade"]}
nota: {aluno["nota"]}\n""")

print("=-"*35, end="=\n")

# Forma compacta
aluno2 = {
    "nome" : "Felipe Farias",
    "idade" : 18,
    "nota" : 77
}

print(f"\n{aluno2}")
print(f"""\nAluno:\n
Nome: {aluno2["nome"]}
Idade: {aluno2["idade"]}
nota: {aluno2["nota"]}\n""")

print("=-"*35, end="=\n")

# .get
aluno3 = {
    "nome" : "David Willian",
    "idade" : 18,
    "nota" : 77
}

print(f"\n{aluno3}\n")
print(aluno3.get("nome"))
print(aluno3.get("idade"))
print(aluno3.get("email")) # devolve none pois nao achou valor da chave
print(aluno3.get("email", "N/A")) # Valor padrao

print()
print("=-"*35, end="=\n\n")


# Percorrendo com .itens
for chave, valor in aluno.items():
    print(f"{chave}:{valor}")