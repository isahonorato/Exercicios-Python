#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo que deseja obter o valor do seno, cosseno e tangente: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {}, tem o SENO de {:.f}'.format(angulo, seno))
print('O ângulo de {}, tem o COSSENO de {:.f}'.format(angulo, cosseno))
print('O ângulo de {}, tem o TANGENTE de {:.f}'.format(angulo, tangente))
