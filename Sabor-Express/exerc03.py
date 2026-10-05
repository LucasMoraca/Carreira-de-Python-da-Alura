# Exercício 1:
numeros = list(range(1, 11))

nomes = ['Lucas', 'Marcos', 'Evair', 'Ademir']

anos = ['2006', '2026']

print('Lista de números: ', numeros)
print('Lista de nomes: ', nomes)
print('Lista de anos: ', anos)

# Exercício 2
frutas = ['Maçã', 'Banana', 'Laranja', 'Uva', 'Abacaxi']

for fruta in frutas:
    print(fruta)

# Exercício 3
soma = 0

for numero in range(1, 11):
    if numero % 2 != 0:
        soma += numero
print('A soma dos números ímpares de 1 a 10 é: ', soma)

# Exercíco 4
for descrescente in range(10, 0, -1):
    print(descrescente)

# Exercício 5
valor = int(input('Informe o valor desejado: '))

for i in range(1, 11):
    print(f'{valor} X {i} = {valor * i}')

# Exercício 6
try: 
    valores = [10, 20, 30, 40, 50]

    soma = 0

    for valor2 in valores:
        soma += valor2

    print(f'A soma dos elementos da lista é: {soma}')

except TypeError:
    print('Erro: a lista contém valores que não são números.')
except Exception as erro:
    print(f'Ocorreu um erro:{erro}')

# Exercício 7
try: 
    valores2 = [10, 20, 30, 40, 50]

    soma2 = 0

    for valor3 in valores2:
        soma2 += valor3

    media = soma2 / len(numeros)

    print(f'A média dos valores é: {media}')

except ZeroDivisionError:
    print('Erro: não é possível calcular a média de uma lista vazia.')
except Exception as erro:
    print(f'Ocorreu um erro: {erro}')
