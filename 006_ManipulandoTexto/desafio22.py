#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas. 
#- Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome: ')).strip()

print(('-')*60)

maiusculo = nome.upper()
minusculo = nome.lower()
quantidade = len(nome) - nome.count(' ')
letras = nome.find(' ')

print ('O seu nome em maiúsculo: ', maiusculo)
print ('O seu nome em minúsculo: ', minusculo)
print ('A quantidade de caracteres que tem o seu nome é {} sem espaços:'.format(quantidade))
print ('O seu primeiro nome tem {} letras'.format(letras))
