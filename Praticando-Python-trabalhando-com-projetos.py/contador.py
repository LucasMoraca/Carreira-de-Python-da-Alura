# Arquivo: contador.py

def contar_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Cria um dicionário contando a frequência de cada palavra
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
        
    return frequencia