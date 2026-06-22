nome = input("Digite seu nome:\n")
anoNascimento = int(input("Digite seu ano de nascimento:\n"))

print(f"\nNome registrado como: {nome}")
print(f"Ano de nascimento registrado: {anoNascimento}\n")

idade = 2026 - anoNascimento

print(f"{nome} tem {idade} anos!\n")
