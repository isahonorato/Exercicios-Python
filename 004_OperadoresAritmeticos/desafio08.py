#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

numero = int(input('Insira um valor em metros para obter a conversão em cm e mm:'))

centimetros = numero * 100
milimetros = numero * 1000

print ('O valor inserido {}, equivale a {} centímetros e {} milímetros'.format(numero, centimetros, milimetros))
