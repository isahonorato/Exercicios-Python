#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele.

dados = input ('Digite algo:')
print ('O tipo primitivo desse valor é: ', type(dados))
print ('Só tem espaços?', dados.isspace)
print ('É um número?', dados.isnumeric)
print ('É alfabético?', dados.isalpha)
print ('É alfanumérico?', dados.isalnum)
print ('Está em maiúsculas?', dados.isupper)
print ('Está em minúsculas?', dados.islower)
print ('Está captalizada?', dados.istitle)