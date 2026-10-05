# Exercício 1
print('========================')
print('Exercício 1')
print('========================')
pessoa = {'nome' : 'Lucas',
          'idade' : '22',
          'cidade' : 'São Paulo'}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])

# Exercício 2
print('========================')
print('Exercício 2')
print('========================')
pessoa['idade'] = 20

pessoa['profissao'] = 'Estagiário'

del pessoa['cidade']

print(pessoa)

# Exercício 3
print('========================')
print('Exercício 3')
print('========================')
quadrados = {
    1: 1**2,
    2: 2**2,
    3: 3**2,
    4: 4**2,
    5: 5**2
}

print(quadrados)

# Exercício 4
print('========================')
print('Exercício 4')
print('========================')

# Criando o dicionário
pessoa = {
    "nome": "Lucas",
    "idade": 20,
    "cidade": "São Paulo"
}

# Verificando se a chave existe
if "idade" in pessoa:
    print("A chave 'idade' existe no dicionário.")
else:
    print("A chave 'idade' não existe no dicionário.")

# Exercício 5
print('========================')
print('Exercício 5')
print('========================')
frase = input("Digite uma frase: ")

palavras = frase.lower().split()

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
