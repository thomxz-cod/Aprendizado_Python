from modules import funcoes
from time import sleep
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

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
    print("""\t\nCardápio Digital\n
0 - Sair
1 - Exibir cardapio completo
2 - Buscar Opção
3 - Adicionar Opção
4 - Atualizar Opção
5 - Deletar Opção
6 - Limpar terminal
""")

    op = int(input("Opção: "))
    match op:
        case 0:
            print("\n\tObrigado, volte sempre!!")
            sleep(3)
            cls()
            break
        case 1:
            funcoes.exibirOpcoes()
            sleep(2)
        case 2:
            funcoes.buscarOpcao()
            sleep(2)
        case 3:
            funcoes.adicionarOpcao()
            sleep(2)
        case 4:
            funcoes.atualizarOpcao()
            sleep(2)
        case 5:
            funcoes.deletarOpcao()
            sleep(2)
        case 6:
            cls()
        case _:
            print("\n\tOpção invalida !!")
            sleep(3)
            continue
