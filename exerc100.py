#Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da
# lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
import random


def sorteia():
    números = []
    for i in range(0, 5):
        números.append(random.randint(1, 100))
    print(f'Os números sorteados foram: \n {números}')
    somaPar(números)


def somaPar(lista):
    sp = 0
    for v in lista:
        if v % 2 == 0:
            sp += v
    print(f'A soma dos números sorteados é: [{sp}]')


sorteia()