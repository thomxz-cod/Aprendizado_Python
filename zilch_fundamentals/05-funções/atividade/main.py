def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    elif len(set(cpf)) == 1:
        return False
    else:
        return True

cpf = input("\nDigite seu cpf: ")
validacao = validar_cpf(cpf)

print(f"""\nCPF: {cpf}
Validação: {validacao}
""")

