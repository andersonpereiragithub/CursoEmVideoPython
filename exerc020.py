#O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

'''nomes = ''
for c in range(0, 4):
    nomes[c] = str(input('Digite o {}o. Nome: ' .format(c + 1)))

random.shuffle(nomes)

for c in range(1, len(nomes)):
    print('{}º a apresentar é: {}' .format(nomes[c]))'''

import random

aluno1 = input("Informe o nome do 1º Aluno: ")
aluno2 = input("Informe o nome do 2º Aluno: ")
aluno3 = input("Informe o nome do 3º Aluno: ")
aluno4 = input("Informe o nome do 4º Aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
