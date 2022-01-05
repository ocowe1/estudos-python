# Fazer um programa que pergunta a hora e baseado no horário dar a saudação apropriada

horario = input("Qual a hora atual? (Digite apenas 2 digitos) ")

if horario.isnumeric():

    horario = int(horario)

    if 0 <= horario <= 11:
        print('Bom dia!')
    elif 12 <= horario <= 17:
        print('Boa Tarde!')
    elif 18 <= horario <= 23:
        print('Boa noite!')
else:
    print('Houve um erro, favor tentar digitar novamente apenas a hora atual.')
