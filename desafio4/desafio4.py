# Faça um programa que peça o primeiro nome do usuario, se tiver 4 letras ou menos escrever que o nome é curto.
# Se tiver entre 5 e 6 letras dizer que é normal, se houver mais que 6 letras dizer que é muito grande.

nome = input('Digite seu primeiro nome: ')

if ' ' in nome:
    print('Por favor digitar apenas o primeiro nome!')
else:
    tamanho = len(nome)

    if tamanho <= 4:
        print('Seu nome é pequeno.')
    elif 5 <= tamanho <= 6:
        print('O tamanho do seu nome é normal.')
    elif tamanho > 6:
        print('Seu nome é muito grande.')
