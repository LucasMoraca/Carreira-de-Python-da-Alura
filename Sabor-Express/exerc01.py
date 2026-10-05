print('Python na Escola de Programação da Alura\n')

nome = input('Informe seu nome: ')
idade = input('Informe a sua idade: ')
print(f'Meu nome é {nome} e tenho {idade} anos')


print('A\nL\nU\nR\nA\n')
print('A','L','U','R','A',sep='\n')

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
