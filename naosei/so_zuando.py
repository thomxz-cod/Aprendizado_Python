nomes = ["Evy", "Thom"]

for nome in nomes:
    print("=-"*8, end="=\n")
    for index, letra in enumerate(nome, 1):
        print("|", f"{index} - {letra}", "\t|")
        pass
    print("=-"*8, end="=\n")

