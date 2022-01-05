# Fazer um programa para que peça um número ao usuário e informar se é par ou impar. Caso não seja um número inteiro
# informar um erro.

num = input("Digite um número: ")

if num.isdigit():
    num = int(num)

    if (num % 2) == 0:
        print('Este número é par.')
    else:
        print('Este número é impar.')
else:
    print('Favor digitar um número inteiro')
    