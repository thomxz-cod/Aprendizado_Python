# Saída esperada 
# 
# Temperaturas registradas: [28.5, 31.0, 25.5, 33.2, 29.8, 27.1] 
# ======= Relatório Climático ======= 
# Média: 29.35°C 
# Máxima: 33.20°C 
# Mínima: 25.50°C 
# Dias acima da média: 3 
# Em ordem crescente: [25.5, 27.1, 28.5, 29.8, 31.0, 33.2]

registros_temperatura = [28.5, 31.0, 25.5, 33.2, 29.8, 27.1]

media = round((sum(registros_temperatura) / len(registros_temperatura)), 2)
maxima = max(registros_temperatura)
minimo = min(registros_temperatura)

contagem = [i for i in registros_temperatura if i > media]
ordem_crescente = sorted(registros_temperatura)

print()
print("="*6, "Relatório Climático", "="*6, f"""
Média: {media}
Máxima: {maxima} 
Mínima: {minimo}
Em ordem crescente: {ordem_crescente}
=================================
""")