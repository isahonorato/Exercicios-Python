#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número: '))

unidade = numero // 1

print('Unidade: '.format())
print('Dezena: '.format())
print('Centena: '.format())
print('Milhar: '.format())