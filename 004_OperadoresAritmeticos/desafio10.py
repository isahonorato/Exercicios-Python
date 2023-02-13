#Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$5,17

dinheiro = float(input('Insira o valor deseja utilizar para a compra de dólares: '))

valorDolar = float(5.17)
divisao = dinheiro / valorDolar 

print ('O seu dinheiro em dolar é', divisao)

