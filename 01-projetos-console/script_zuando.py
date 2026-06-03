# nome = input("Bem vindo, qual seu nome? ")
# print(f"Olá {nome}")

print("\tSistema de Calculadora entre dois numeros\n")

print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão\n")

value = int(input("Digite a operação: "))
num1 = int(input("Primeiro numero: \n"))
num2 = int(input("Segundo numero: \n"))

soma = 0

def adicao():
    return num1 + num2

def subtracao():
    return num1 - num2

def multiplicacao():
    return num1 * num2

def divisao():
    return num1 / num2



match value:
    case 1:
        soma = adicao()
        print(f"Resultado: {soma}")
    case 2:
        soma = subtracao()
        print(f"Resultado: {soma}")
    case 3:
        soma = multiplicacao()
        print(f"Resultado: {soma}")
    case 4:
        soma = divisao()
        print(f"Resultado: {soma}")
    case _:
        print("Alguma coisa deu errado fei")
