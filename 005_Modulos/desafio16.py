#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua proporção inteira.

import random, math

numero = random.random()

print('O número digitado tem a parte inteira de {}'.format(math.ceil(numero)))