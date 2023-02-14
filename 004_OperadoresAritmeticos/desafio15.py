#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

kmRodado = float(input('Insira a quantidade de KMs percorridos pelo carro alugado: '))
diasAluguel = int(input('Insira a quantidade de dias alugados: '))

valor = (diasAluguel * 60) + (kmRodado * 0.15)

print ('De acordo com os {}KMs percorridos e com os {} dias usados, o valor total do aluguel é R${:.2f}'.format(kmRodado, diasAluguel, valor))