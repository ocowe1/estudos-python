# Fazer um programa que pergunta a hora e baseado no horário dar a saudação apropriada

horario = input("Qual a hora atual? (0 - 23) ")

if horario.isdigit():

    horario = int(horario)

    if horario < 0 or horario > 23:
        print("O horário deve estar entre 0 e 23")
    else:
        if 0 <= horario <= 11:
            print('Bom dia!')
        elif 12 <= horario <= 17:
            print('Boa Tarde!')
        elif 18 <= horario <= 23:
            print('Boa noite!')
else:
    print('Houve um erro, favor tentar digitar novamente apenas a hora atual.')
