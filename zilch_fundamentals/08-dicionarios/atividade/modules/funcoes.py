cardapio = {
    'Lasanha' : { 'categoria' : 'Comes' , 'preco' : 6000.0 },
    'Burger':{ 'categoria' : 'Comes' , 'preco' :  300.0 },
    'Gin':{ 'categoria' : 'Bebes' , 'preco' :   12.0 },
    'Ice':{ 'categoria' : 'Bebes' , 'preco' :   16.0 }
}

###################################################################################

def exibirOpcoes():   #  exibe todas as opções do cardapio
    print("\n\tCardapio Completo\n\n===Comes===")
    for opcao, dados in cardapio.items():
        if dados['categoria'] == 'Comes':
            print(f"{opcao:10} | R$ {dados['preco']:-8}")
    print("\n===Bebes===")
    for opcao, dados in cardapio.items():
        if dados['categoria'] == 'Bebes':
            print(f"{opcao:10} | R$ {dados['preco']:-8}")
    print("\n===Others===")
    for opcao, dados in cardapio.items():
        if dados['categoria'] != 'Comes' and dados['categoria'] != 'Bebes':
            print(f"{opcao:10} | R$ {dados['preco']:-8}")
            
###################################################################################

def buscarOpcao():    # encontra uma opção expecifica do cardapio
    nome = input("\nDigite o nome do prato: ")
    dados = cardapio.get(nome)
    if dados:
        print(f"\n{nome:10} | R$ {dados['preco']:-8}")
    else:
        print("\nOpção não encontrada")
    # for opcao, dados in cardapio.items():
    #     if nome == opcao.lower():
    #         print(f"\n{opcao:10} | R$ {dados['preco']:-8}")

###################################################################################

def adicionarOpcao():   # adiciona uma nova opção no cardapio
    nome = input("\nDigite o nome da nova opção: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    cardapio.update({nome:{'categoria':categoria, 'preco':preco}})

###################################################################################

def atualizarOpcao():   # Atualiza uma opção no cardapio
    nome = input("\nDigite o nome da opção que deseja atualizar: ")
    confirmacao = cardapio.get(nome)
    if confirmacao:
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        cardapio.update({nome:{'categoria':categoria, 'preco':preco}})
    else:
        print("Produto não encontrado! ")

###################################################################################

def deletarOpcao(): # Deleta opção
    nome = input("\nDigite o nome da opção que deseja deletar: ")
    confirmacao = cardapio.get(nome)
    if confirmacao:
        del cardapio[nome]
    else:
        print("\nOpção não encontrada")
    
if __name__ == "__main__":
    print("\n\tRode o main.py!!")
