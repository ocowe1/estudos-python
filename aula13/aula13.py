while True:
    cpf = input('Digite um cpf: ')
    tam_cpf = len(cpf)

    if tam_cpf < 10:
        print('Seu CPF é inválido')
        break

    novo_cpf = cpf[:-2]
    total = 0

    reverso = 10
    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * reverso
        reverso -= 1

        if reverso < 2:
            reverso = 11

            d = 11 - (total % 11)

            if d > 9:
                d = 0

            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('Válido')
    else:
        print("Inválido")
