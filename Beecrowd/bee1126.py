diaCompra = input()
prazoEntregue = int(input())


diasDaSemana = ['domingo', 'segunda', 'terca',
                'quarta', 'quinta', 'sexta', 'sabado']

if prazoEntregue == 0:
    print(f"chega hoje!")
else:
    x = diasDaSemana.index(diaCompra)
    if x+prazoEntregue > 6:
        restantes = (prazoEntregue - (6 - x))-1
        localizacao = diasDaSemana[restantes]
    else:
        localizacao = x+prazoEntregue
        localizacao = diasDaSemana[localizacao]
    print(f"sera entregue {localizacao}")