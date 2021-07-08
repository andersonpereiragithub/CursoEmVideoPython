#Um professor quer sortear um dos seus quatro alunos para apagar o
#quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
#o nome do escolhido.
import random

aluno1 = input("Informe o nome do 1º Aluno: ")
aluno2 = input("Informe o nome do 2º Aluno: ")
aluno3 = input("Informe o nome do 3º Aluno: ")
aluno4 = input("Informe o nome do 4º Aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido é: {}' .format(random.choice(lista)))