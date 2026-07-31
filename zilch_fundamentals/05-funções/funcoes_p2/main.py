# Exemplo real: IMC com funções separadas
def calcular_imc(peso, altura):
    imc = round((peso / (altura ** 2)), 2)
    return imc

def classificar_imc(imc):
    if imc <= 18.5:
        return "Abaixo do peso!"
    elif imc <= 25:
        return "Peso normal"
    elif imc <= 30:
        return "Acima do peso"
    else:
        return "Obesidade"

print("\n\t=== IMC ===\n")
nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
print(f"\n{nome}: IMC {imc} - {classificacao}")