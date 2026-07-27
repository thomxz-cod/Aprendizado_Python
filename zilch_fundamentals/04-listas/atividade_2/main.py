dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"""
a) Primeiros 3: {dados[:3]}
b) Últimos 3: {dados[-3:]}
c) Índices pares: {dados[::2]}
d) Índices ímpares: {dados[1::2]}
e) Invertida: {dados[::-1]}
f) Elementos do meio: {dados[3:7]}
""")