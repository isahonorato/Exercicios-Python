#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número:'))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print ('O número digitado foi {}, o dobro do número é {}, o triplo é {}, e a raiz quadrada {}'.format(numero, dobro, triplo, raizQuadrada))