#!/usr/bin/env python3

import os

os.system("cls" if os.name == "nt" else "clear")

cor = input("Digite a cor do semáforo:\n\n(verde)\n(amarelo)\n(vermelho)\n\n").lower()
pessoa = input("\nDigite se você é pedestre ou motorista:\n\n").lower()

print()
print("="*45)
if cor == "verde" and pessoa == "motorista":
    print("\nPode avançar!\n")
elif cor == "verde" and pessoa == "pedestre":
    print("\nEspere o sinal ficar vermelho.\n")
elif cor == "amarelo":
    print("\nAtenção! Prepare-se para parar.\n")
elif cor == "vermelho" and pessoa == "motorista":
    print("\nPare! Aguarde o sinal verde.\n")
elif cor == "vermelho" and pessoa =="pedestre":
    print("\nVocê pode atravessar com atenção.\n")
else:
    print("\nCor invalida. Digite verde, amarelo ou vermelho.\n")
print("="*45)

