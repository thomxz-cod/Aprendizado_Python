produtos = [      # lista de dicionarios
    {
        'nome'       : 'notebook',
        'preco'      : 3500.0,
        'categoria'  : 'eletronico'
    },
    {
        'nome'       : 'Mouse',
        'preco'      : 89.90,
        'categoria'  : 'eletronico'
    },
    {
        'nome'       : 'Cadeira',
        'preco'      : 999.99,
        'categoria'  : 'mobilia'
    }
]

# Filtrar eletronicos dos dicionarios 
eletronic1 = [p for p in produtos if p['categoria'] == 'eletronico']   # forma compacta 
print(f"{eletronic1}\n")

eletronic2 = []      # forma descompacta
for produto in produtos:
    if produto['categoria'] == "eletronico":
        eletronic2.append(produto)
print(f"{eletronic2}\n")


# Ordenar por preço
ordem = sorted(produtos, key=lambda p: p['preco'])
for p in ordem:
    print(f"{p['nome']:15} R$ {p['preco']:.2f}")