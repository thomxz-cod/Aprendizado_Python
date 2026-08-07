# Input = python é incrível e python é fácil de aprender e usar python

# Output
# palavra e vezes que a palavra foi digitada
# Total de palavras:        11 
# Palavras únicas:          8 
# Palavra mais frequente:   python (3x)

# variables
# sentence = frase
# word = palavra

sentence = input("\nDigite a frase: ")

# split() divide uma string em uma lista de substrings menores com base em um caractere delimitador ou separador e retorna uma lista.

count = {}
for word in sentence.split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

WORD_MAX = max(count, key=count.get) # o key significa critério de ordenação, voce precisa passar count.get para que ele analize o valor invez da chave

print("\n\t=== Frequência de palavras ===\n")

for word, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
    print(f"{word:15}:{value}x")

print(f"""
Total de palavras:          {len(sentence.split())}
Palavras únicas:            {len(count)}
Palavra mais frequente:     {WORD_MAX} ({count[WORD_MAX]}x)
""")
