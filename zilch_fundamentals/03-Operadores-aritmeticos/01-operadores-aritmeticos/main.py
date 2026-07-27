numero1, numero2 = int(input("Numero 1: ")), int(input("Numero 2: "))

print(f"{numero1} mais {numero2} é igual a: {numero1 + numero2}")
print(f"{numero1} menos {numero2} é igual a: {numero1 - numero2}")
print(f"{numero1} multiplicado por {numero2} é igual a: {numero1 * numero2}")
print(f"{numero1} dividido por {numero2} é igual a: {numero1 / numero2}")
print(f"{numero1} dividido por (ele descarta o resto caso seja numero float) {numero2} é igual a: {numero1 // numero2}")
print(f"Resto da divisão é {numero1 % numero2} ")
print(f"2 elevado a 8 é igual a: {2 ** 8}")


####

saldo = 1000
saldo += 500 #saldo = saldo + 500 > 1500
saldo -= 200 # 1300
saldo *= 2 #2600
print(saldo)
