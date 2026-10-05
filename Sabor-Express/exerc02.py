# Exercício 1
numero = int(input("Insira um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Exercício 2
idade = int(input('Insira a sua idade: '))

if idade <= 12:
    print('Criança')
elif idade > 18:
    print('Adulto')
else:
    print('Adolescente')

# Exercício 3
usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Usuário ou senha incorretos.")

# Exercício 4
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x > 0 and y > 0:
    print("O ponto está no Primeiro Quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no Segundo Quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no Terceiro Quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no Quarto Quadrante.")
else:
    print("O ponto está localizado no eixo ou na origem.")
