numeros = input()
tratamento = numeros.split()

A = int(tratamento[0])
B = int(tratamento[1])

if (A % B == 0 or B % A == 0):   
        print('Sao Multiplos') 
else:
        print('Nao sao Multiplos')
