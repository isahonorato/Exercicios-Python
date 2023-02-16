#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

catetoOposto = float(input('Insira o comprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Insira o comprimento do Cateto Adjacente: '))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print('A hipotenusa mede: {:.2f}'.format(hipotenusa))