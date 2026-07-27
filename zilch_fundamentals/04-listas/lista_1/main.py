notas = [5.3, 7, 9.7, 2.4, 10.0]

print(f"""\nlista - {notas}\n
indice  0 == {notas[0]}\n
indice  1 == {notas[1]}\n
indice -1 == {notas[-1]}\n
indice -2 == {notas[-2]}\n
""")

notas[1] = 7.5
print(f"indice 1 atualizado == {notas[1]}")