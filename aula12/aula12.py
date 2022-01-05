# Operadores Ternários

# logged_user = False
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'


idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Digite apenas números')
else:
    idade = int(idade)
    acesso = (idade >= 18)
    msg = "Pode acessar" if acesso else 'Não pode acessar'
    print(msg)

# print(msg)
