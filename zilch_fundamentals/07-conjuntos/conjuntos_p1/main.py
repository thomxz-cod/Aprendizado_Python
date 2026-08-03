"""
    Os conjuntos nao aceitam elementos iguais
"""

numeros = {1, 2, 3, 2, 1}
print(numeros) # {1, 2, 3}


# Remover duplicatas de listas set()
lista = [1, 2, 3, 3, 5, 5, 7, 9]
print(set(lista))



# Operações em conjuntos
a = {1,2,3,4}
b = {3,4,5,6}

print(a | b) # une os conjuntos e ja exclui os elementos iguais

print(a & b) # interseção ( mostra os item que se repetem )

print(a - b) # diferença ( oq "a" tem que "b" nao tem )
print(b - a) # diferença ( oq "b" tem que "a" nao tem )

print(a ^ b) # diferença simetrica ( diferença entre os dois ao mesmo tempo )