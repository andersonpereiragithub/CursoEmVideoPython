#Escreva um programa que leia dois números inteiros e
# compare-os, mostrando na tela uma mensagem:
#O primeiro valor é Maior; O segundo valor é Maior; Não existe
#valor maior, os dois são iguais.

num1 = int(input('Inserir 1º número: '))
num2 = int(input('Inserir 2º número: '))

if num1 > num2:
    print('O {} é maior do que o {}.' .format(num1, num2))
elif num1 < num2:
    print('O {} é maior do que o {}.' .format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais.')