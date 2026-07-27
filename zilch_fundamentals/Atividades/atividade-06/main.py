continuar = "s"

while continuar == "s":
    num1 = int(input("Informe um número inteiro: "))
    
    for i in range(1, 11):
        print(f"{num1} x {i} = {num1 * i}")

    continuar = input("Deseja ver outra tabuada? (s/n)\n").lower()


    if continuar != "n" and continuar != "s":
        print("Opção invalida. Processo encerrado!")

