nome = "Vinicius"
idade = 23
altura = 1.75
peso = 65
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} nasceu em {nascimento}, tem {idade} anos de idade, possui {altura} de altura e pesa {peso}kg, seu imc é de {imc:.2f}')
