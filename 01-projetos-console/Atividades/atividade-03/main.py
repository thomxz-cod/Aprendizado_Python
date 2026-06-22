nome = input("Digite seu nome: ")
idade = int(input("digite sua idade: "))
tempoEstudando = int(input("Digite a quantos anos você estuda?\n"))
linguaPreferida = input("Qual a sua linguagem de programação favorita?\n")
nota = int(input("""\nNota para o fichario. Onde: 
0 a 4 = Ruim
5 a 7 = Mediano
8 a 10 = Bom
"""))
if 0 <= nota <= 4:
    nota = "Ruim"
elif 5 <= nota <= 7:
    nota = "Mediano" 
elif 8 <= nota <=10:
    nota = "Bom"
else:
    ValueError

print("="*45)
print("\tFichario")
print("="*45)
print(f"""
Nome: {nome}
Idade: {idade}
Anos estudando: {tempoEstudando} ano(s)
Linguagem Fav.: {linguaPreferida}
Nota: {nota}
""")
print("="*45)
