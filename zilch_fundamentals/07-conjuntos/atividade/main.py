produtos = [ # ID - nome(produto) - tempoGarantia(meses) - tempoUso(meses) - situação(vencida/em garantia)
    (1001, "HeadSeat", 24, 18),
    (1002, "Nootpad", 12, 14),
    (1003, "Monitor", 36, 10),
    (1004, "Teclado", 12, 16),
    (1005, "Fariaç", 300, 216)
]

em_garantia = 0

print("Código  -    Nome    -  Garantia  -    Uso    -    Situação\n")
for i in produtos:
    garantia = i[2]
    tempoUso = i[3]
    if garantia >= tempoUso:
        sitacao = f"Em garantia ({garantia - tempoUso} meses restantes)"
        em_garantia += 1
    else:
        sitacao = f"Garantia Vencida ({abs(garantia - tempoUso)} meses atras)" # função abs retorna numero absoluto (positivo)
    print(f" {i[0]}      {i[1]}         {i[2]}m        {i[3]}m       {sitacao}")

print(f"""
Resumo:
Total: {len(produtos)}
Em garantia: {em_garantia}
Vencidos: {len(produtos) - em_garantia}""")
