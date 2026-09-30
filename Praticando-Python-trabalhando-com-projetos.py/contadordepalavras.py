# precisa criar a configuração do contador para rodar, seria algo meio que orientado a objeto, mas não é necessário criar uma classe, apenas uma função que recebe a frase e retorna a quantidade de palavras.

from contador import contar_palavras

frase = input("Digite uma frase: ").strip()

if not frase:
    print("Nenhuma frase foi digitada.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de palavras:")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
    else:
        print("Nenhuma palavra encontrada na frase.")