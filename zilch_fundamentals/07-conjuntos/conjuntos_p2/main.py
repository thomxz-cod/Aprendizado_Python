# CASO 1: detectar CPFs duplicados em cadastro

cpfs = ["123.456.789-00", "987.654.321-00",
        "123.456.789-00", "111.111.111-00"]

unicos = set(cpfs)
num_duplicados = len(cpfs) - len(unicos)

print(f"""Total de cadastrados: {len(cpfs)}
CPFs unicos: {len(unicos)}
Quantidade de duplicados: {num_duplicados}""")

###########################################################################

# CASO 2: Tuplas garantem que ningem mude as posições

SENAI_SIG = (-15.8311, -48.0500) # Constante
lat, lon = SENAI_SIG

print(f"\nSENAI esta em : {lat}, {lon}")

###########################################################################

# CASO 3: Função que retorna multiplos valores

def estastisticas(notas): # retorna media, maior e menor nota como tupla
    return round((sum(notas)/len(notas)), 2), max(notas), min(notas)

notas = [8.9, 7.0, 9.2, 6.5]
media, maior, menor = estastisticas(notas)
print(f"""\nMedia: {media}
Maior: {maior}
Menor: {menor}

Type: {type(estastisticas(notas))}""")
