alunos = ["Carlos",
          "Ana",
          "Diana",
          "Bruno",
          "Toin"]

print(f"\nantes == {alunos}")
# append, insert, remove, pop

# append
alunos.append("Felipe Farias") # adiciona no fim da lista
print(f"\ndepois do append == {alunos}")

# insert
alunos.insert(0, "David Willian") # adiciona em qualquer indice da lista
print(f"\ndepois do insert == {alunos}")

# remove
alunos.remove("Diana") # remove todos os elementos "Dianas"
print(f"\ndepois do remove == {alunos}")

# pop
ultimo = alunos.pop() # remove e da uma saida, que pode ser salvo em uma variavel, indice padrão é -1(ultimo)
print(f"\ndepois do pop == {alunos} | removido: {ultimo}")


##############################################################################################################################################################

# sort vs sorted

# sorted() cria e retorna uma nova lista ordenada sem mexer na original.
nova_lista_alunos = sorted(alunos)
print(f"\nOriginal = {alunos} | Sorted = {nova_lista_alunos}              #  Listas diferentes na memoria")

# sort() altera aleatoriamente a lista original e retorna None
print(f"\nResposta do sort = {alunos.sort()} | Lista atualizada{alunos}                                              #  Muda a lista original")

###############################################################################################################################################################