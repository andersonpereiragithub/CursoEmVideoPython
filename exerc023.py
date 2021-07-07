#Faça um programa que leia um número de 0 a 9999 e mostre
#na tela cada um dos dígitos separados.
#Exemplo: 1834 unidade: 4 dezena 3 centena 8 milhar 1

num = int(input('Infome um número: '))
#n = str(num) aqui da erro se o número for menor que milhar
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}' . format(num))
print('Unidade: {}' .format(u))
print('Dezena {}' .format(d))
print('Centena {}' .format(c))
print('Milhar {}' . format(m))
