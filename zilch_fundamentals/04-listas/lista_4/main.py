matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(f"Elemento 2 da lista de indice 1    {matriz[1][2]}") # busca na lista dentro da lista
print()

# enumerate
frutas = ["maçã", "laranja", "uva"]
for i, fruta in enumerate(frutas):
    print(f"O indice {i} contem o elemento {fruta}")
print()


# zip ( junta duas lista por indice, indice0_lista1:indice0_lista2 )
nomes = ["Toin", "Debora", "Sara"]
notas = [100, 67, -9999]
for nome, nota in zip(nomes, notas):
    print(f"nome: {nome} | nota: {nota}")
print()
