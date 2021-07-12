#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Quantidade de elementos: '))
penultimo = 0
ultimo = 1
flag = 1
while flag < n:
    if penultimo == 0:
        print('{} - {}'.format(penultimo, ultimo), end='')
        penultimo += ultimo
        flag += 1
    else:
        print(' - {}'.format(ultimo), end='')
        ultimo += penultimo
        penultimo = ultimo - penultimo
        flag += 1