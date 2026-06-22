# sequencias = [
#     [3, 4, 5],
#     [2, 2, 5],
#     [7, 8, 10],
#     [1, 3, 5],
#     [6, 6, 6],
#     [4, 4, 8],
#     [9, 12, 15],
#     [5, 7, 13],
#     [8, 10, 12],
#     [2, 3, 4],
#     [10, 10, 19],
#     [3, 6, 9],
#     [11, 14, 20],
#     [5, 5, 9],
#     [7, 7, 14],
#     [12, 13, 24],
#     [4, 5, 6],
#     [1, 1, 1],
#     [15, 20, 25],
#     [3, 8, 12]
# ]

# listaTriangulo = []
# for index, numero in enumerate(sequencias):
#     lado1 = numero[0]
#     lado2 = numero[1]
#     lado3 = numero[2]
    
#     if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
#         listaTriangulo.append(True)
#     else:
#         listaTriangulo.append(False)


# print(f"{listaTriangulo}.")



"""

        ATIVIDADE

"""

lado1 = float(input("informe o valor do primeiro lado: "))
lado2 = float(input("informe o valor do segundo lado: "))
lado3 = float(input("informe o valor do terceiro lado: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
        

    print(f"É um triagulo e é do tipo {tipo}!")
else:
    print("""Isso não é um triângulo válido
\nPrograma encerrado..
""")
