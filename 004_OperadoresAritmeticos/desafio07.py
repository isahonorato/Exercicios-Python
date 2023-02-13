#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nomeAluno = (input('Digite o nome do aluno'))
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = nota1 + nota2
resultado = media / int(2)

print ('A média do(a) aluno(a) {}, é {}'.format(nomeAluno, resultado))
