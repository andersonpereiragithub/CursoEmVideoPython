#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Informe o número: '))
num2 = num
f = 1
print('Calculando {}! = ' .format(num), end='')
while num2 > 0:
    print('{}' .format(num2), end='')
    print(' x ' if num2 > 1 else ' = ', end='')
    f *= num2
    num2 -= 1
print(f)
