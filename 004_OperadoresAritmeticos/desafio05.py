#Faça um programa que leia um número inteiro e mostre o seu sucessor e antecessor

numero = int(input('Digite um número inteiro e descubra o seu antecessor e sucessor:'))

antecessor = numero - int(1)
sucessor = numero + int(1)

print ('O número digitado foi {}, o seu sucessor é {}, e o seu antecessor é {}'.format(numero, sucessor, antecessor))