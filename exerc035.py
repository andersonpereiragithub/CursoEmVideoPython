#Desenvolva um programa que leia o comprimento de três
#retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Informe o tamanho da primeira Reta: '))
r2 = float(input('Informe o tamanho da primeira Reta: '))
r3 = float(input('Informe o tamanho da primeira Reta: '))

if r1 + r2 >= r3 and r2 + r3 >= r1 and r3 + r1 >= r2:
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')