# Criar tupla
coordenada = (-15.77, -47.92)
rgb = (255, 0, 0)
unit = (42,) 

lat, lon = coordenada
print(f'Brasília: {lat},{lon}')

# Retorno múltiplo de função
def minmax(lista):
    return min(lista), max(lista)

notas = (7.5, 9.0, 5.5, 8.2)
menor, maior = minmax(notas)
print(f'Menor: {menor} Maior: {menor}')
