# if simples 
idade = int(input('idade; '))

if idade >= 18:
    print('maior de idade')
    print('acesso permitido')

# if / else 
nota = float(input('nota: '))

if nota >= 7.0:
    print('Aprovado')

else:
    print('Reprovado')

# if / elif / else
nota = float(input('Nota do aluno: '))

if nota >= 9.0:
    conceito = 'A'
    situacao = 'excelente'
elif nota >= 7.0:
    conceito = 'D'
    situacao = 'aprovado'
elif nota >= 5.0:
    conceito = 'C'
    situacao = 'recuperação'
else:
    conceito = 'D'
    situacao = 'reprovado'

print(f'conceito: {conceito} | situação: {situacao}')