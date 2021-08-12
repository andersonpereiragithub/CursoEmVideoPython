#Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que
# analisar todos os valores e dizer qual deles é o maior.
from random import randint
def maior(* num):
    m = 0
    for v in num:
        if v > m:
            m = v
    print(f'O maior número entre {num} é [{m}].')


maior(23, 5551, 644, 3, 4, 88)

def maior2(num):
    m = 0
    for v in num:
        if v > m:
            m = v
    print(f'O maior número entre {num} é [{m}].')

#Não funciona uma FUNÇÃO que recebe vários números e uma LISTA.
numeros = []
for i in range(0, 10):
    numeros.append(randint(1, 3000))
maior2(numeros[:])