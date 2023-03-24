variavel = input()
variavelDois = input()
vari = variavel.split()
variDois = variavelDois.split()


cod = vari[0]
quantidade = int(vari[1])
valor = float(vari[2])
resultado = (quantidade * valor)


codDois = variDois[0]
quantidadeDois = int(variDois[1])
valorDois = float(variDois[2])
resultadoDois = (quantidadeDois * valorDois)

sun = (resultado + resultadoDois)

print (f'VALOR A PAGAR: R$ {sun:.2f}')