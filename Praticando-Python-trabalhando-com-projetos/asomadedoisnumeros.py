def somar (a, b):
    return a + b

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print(f"A soma de {num1} e {num2} é: {resultado}")
except ValueError:
    print('Erro: Por favor, digite apenas números válidos.')