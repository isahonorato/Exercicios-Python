#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o seu salário para calcularmos o aumento de 15%: '))

salarioNovo = salario + (salario * 15 / 100)

print ('O seu salário antigo era de R${} e o novo após o reajuste de 15% é de R${}'.format(salario, salarioNovo))

