P1 = float(input('Informe a nota P1: '))
P2 = float(input('Informe a nota P2: '))
P3 = float(input('Informe a nota P3: '))

media = (P1 + P2 + P3)/3
print(f'Média: {media: .2f}\n')

if media < 5:
    print('Reprovado')
elif media >= 7:
    print('Aprovado')
else:
    print('Recuperação')
