#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input('Insira o preço do produto para saber o valor final após aplicar o desconto de 5%: '))

descontoProduto = produto * 5
valorFinal = descontoProduto / 100
produtoComDesconto = produto - valorFinal

print ('Valor do produto SEM desconto: ', produto)
print ('Valor do produto COM desconto: ', produtoComDesconto)