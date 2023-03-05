nome = str(input())
salarioFixo = float(input())
totalVendasDinheiro = float(input())

valorFinal = (((totalVendasDinheiro * 15) / 100) + salarioFixo)

print(f'TOTAL = R$ {valorFinal:.2f}')