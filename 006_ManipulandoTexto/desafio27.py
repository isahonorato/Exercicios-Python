#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome.

nome = str(input('Digite o seu nome completo: ')).strip()
nomePessoa = nome.split() 

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)]-1))



