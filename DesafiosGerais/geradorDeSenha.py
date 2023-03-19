#Faça um programa que gere para o usuário uma senha aleatória

import random

caracteresMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteresMin = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteresEsp = "!@#$%&*"

gerador = caracteresMax + caracteresMin + numeros + caracteresEsp
digitos = 15

senha = "".join(random.sample(gerador, digitos))

print ("Senha: " + senha)