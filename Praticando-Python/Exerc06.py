hora_atual = int(input('Informe a hora atual (formato 24 horas): '))

if 8 <= hora_atual < 18:
    print('Acesso permitido')
else:
    print('Acesso negado!')
