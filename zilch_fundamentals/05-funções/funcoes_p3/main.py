def minha_funcao():
    variavel_local = "So existo aqui dentro"
    print(variavel_local) # funciona pois esta no mesmo bloco da variavel

minha_funcao()
# print(variavel_local) # nao conhece a variavel - NameError - name 'variavel_local' is not defined

# Variavel global
mensagen = "Sou global"

def outra_funcao():
    print(mensagen) # pode ler as variaveis globais

outra_funcao()
