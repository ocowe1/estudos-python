nome = "Vinicius"
idade = 22
altura = 1.75
e_maior = idade > 18
peso = 65
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É Maior:', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{2} {0} {0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {imc}'.format(n=nome, i=idade, imc=imc))
