distancia = float(input('Informe a distância percorrida em km: '))

if distancia < 100:
    print('Valor do pedágio: R$ 10,00')
elif distancia > 200:
    print('Valor do pedágio: R$ 30,00')
else:
    print('Valor do pedágio: R$ 20,00')
