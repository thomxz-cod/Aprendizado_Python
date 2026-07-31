# função simples - sem parâmetros 
def saudar():
    print('Olá! Bem-vindo ao Senai!')
    print('Bons estudos!')

saudar() # chamando a função 
saudar() # pode chamar função varias vezes 

# com parâmetros 
def saudar_pessoas(nome, curso):
    print(f'olá, {nome}')
    print(f'Ben vindo ao curso de {curso}')
saudar_pessoas('TOIN', 'python')

# parametro com valor padrao
def potenia(base, expoente=2):
    return base ** expoente

print(potenia(5))
print(potenia(2,8)) # o expoente por padrao vale 2, mas foi passado 8 como argumento
