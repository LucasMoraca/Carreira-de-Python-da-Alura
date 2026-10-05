altura = float(input('Informe a altura em metros: '))

peso = float(input('Informe o peso em quilogramas: '))

IMC = peso / (altura**2)
print(f'Seu IMC é: {IMC: .2f}')

if IMC < 18.25:
    print('Abaixo do peso')
elif IMC < 25:
    print('peso normal')
else: 
    print('Acima do peso')
