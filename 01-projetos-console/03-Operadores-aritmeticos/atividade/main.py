num1 = float(input('digite um numero: '))
num2 = float(input('digite um numero: '))
op = input('operação (+ - * /): ')

if op == "+":
    soma = num1 + num2
    print(f"{num1} {op} {num2} = {soma}")
elif op == "-":
    soma = num1 - num2
    print(f"{num1} {op} {num2} = {soma}")
elif op == "*":
    soma = num1 * num2
    print(f"{num1} {op} {num2} = {soma}")
elif op == "/":
    if num2 == 0:
        print("Não é possivel dividir nenhum numero por 0!")
    else:
        soma = num1 / num2
        print(f"{num1} {op} {num2} = {soma}")
else:
    print("Operação invalida!")
