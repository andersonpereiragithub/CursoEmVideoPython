#Crie um programa que leia um númeor e mostre na tela se ele é
#PAR ou ÍMPAR.

num = int(input('Digite um número: '))
if(num % 2) == 0:
    print('O {} é PAR'.format(num))
print('O {} é ÍMPAR'.format(num))