def contar_palavras(frase):
    if frase is None:
        return 0
    palavras = frase.split()
    return len(palavras)
