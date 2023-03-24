ABC = input()
tratamento = ABC.split()

pi = 3.14159

A = float(tratamento[0])
B = float(tratamento[1])
C = float(tratamento[2])


print(f'TRIANGULO: {A * C / 2:.3f}')
print(f'CIRCULO: {pi * C ** 2:.3f}')
print(f'TRAPEZIO: {(A + B) * C / 2:.3f}')
print(f'QUADRADO: {B ** 2:.3f}')
print(f'RETANGULO: {A * B:.3f}')



