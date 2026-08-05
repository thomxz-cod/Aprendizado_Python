from modules import funcoes
from time import sleep
import os

# status_code = 404

# match status_code:
#     case 200:
#         print("Success")
#     case 400:
#         print("Bad Request")
#     case 404:
#         print("Not Found")
#     case _:
#         print("Unknown Status")  # Catch-all wildcard

while True:
    print("""
0 - Sair
1 - Exibir cardapio completo
2 - Buscar Opção
3 - Adicionar Opção
4 - Atualizar Opção
5 - Remover Opção
""")

    op = int(input("Opção: "))
    match op:
        case 0:
            break
        case 1:
            funcoes.exibirOpcoes()
        case _:
            print("\n\tOpção invalida !!")
            sleep(5)
            continue