nome = input("Digite o nome do produto: ")
valor_unitario = float(input("Digite o valor de apenas 1 do produto: "))
quantidade = int(input("Digite a quantidade de produtos sendo levados: "))

calculo = valor_unitario * quantidade

print(f"""
Produto: {nome}
Valor final: {calculo}
""")
