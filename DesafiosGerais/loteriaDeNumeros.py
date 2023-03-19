#Crie um programa que o usuário digite um número e o programa diga se ele acertou na loteria ou não.

import random

print("Bem vindo a Loteria!")

numeroUsuario = 0

while (numeroUsuario > 10 or numeroUsuario < 1):
    numeroUsuario = input("Escolha um número de 1 a 10: ")
    numeroUsuario = int(numeroUsuario)

if (numeroUsuario > 10 or numeroUsuario < 1):
    print("Você escolheu um número INVÁLIDO!")

RandomNumero = random.choice(range(1, 11))
if (numeroUsuario == RandomNumero):
    print("PARABÉNS, VOCÊ ACERTOU NA LOTO!!!")
    print("O número sorteado foi:", RandomNumero)
if(numeroUsuario != RandomNumero):
    print("Você perdeu!")
    print("O número sorteado foi:", RandomNumero)
