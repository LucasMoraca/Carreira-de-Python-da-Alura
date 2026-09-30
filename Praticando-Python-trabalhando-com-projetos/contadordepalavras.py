# precisa criar a configuração do contador para rodar, seria algo meio que orientado a objeto, mas não é necessário criar uma classe, apenas uma função que recebe a frase e retorna a quantidade de palavras.

from contador import contar_palavras

frase = input('Digite uma frase:')
quantidade = contar_palavras(frase)
print(f'A frase digitada possui {quantidade} palavras.')