#Escreva um programa que converta uma temperatura digitada em C e converta para F

celsius = float(input('Informe a temperatura em C°: '))

fahrenheit = ((celsius * 9) / 5) + 32

print('A temperatura de {} C° equivale a {} F°'.format(celsius, fahrenheit))


