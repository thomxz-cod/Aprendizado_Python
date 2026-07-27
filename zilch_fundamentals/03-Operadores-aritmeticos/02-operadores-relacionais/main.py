numero1 = 10 
numero2 = 7 

print(numero1 == numero2) # false - igual a 
print(numero1 != numero2) # true - diferente de 
print(numero1 > numero2) # true - maior que 
print(numero1 < numero2) # false - menor que 
print(numero1 >= numero2) #true - maior ou igual
print(numero1 <= numero2) #false - menor ou igual

# comparando string
nome = 'toin'
print(nome == 'toin') # true 
print(nome == 'Toin') # false (case-sensitive)

# Operadores logicos; and, or not
idade = 20 
tem_habilitacao = True

# and: as duas condições precisam ser verdadeiras 
pode_dirigir = idade >= 18 and tem_habilitacao
print(pode_dirigir) #true

nota = 6.5
freq = 70

# or: PELO MENOS UMA precisa ser verdade 
precisa_recuperar = nota < 7.0 or freq < 75
print(precisa_recuperar) #true

# not: inverte 
print(not True) # false
print(not False) # true 

