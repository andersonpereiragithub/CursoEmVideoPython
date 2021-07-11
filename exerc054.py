#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.
import datetime

menorIdade = 0
maiorIdade = 0
anoAtual = datetime.date.today().year

for c in range(1, 8):
    nascimento = int(input('Ano de nacimento da {}a. Pessoa: ' .format(c)))
    if (anoAtual - nascimento) < 18:
        menorIdade += 1
    else:
        maiorIdade += 1

print('{} são maiores de idade. \n {} são menores de idade: '.format(maiorIdade, menorIdade))