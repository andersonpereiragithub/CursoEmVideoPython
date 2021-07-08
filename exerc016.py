#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
#a sua porção Inteira.
#Exemplo: Digite um ´numeor: 6.127
import math
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}. '.format(num, math.trunc(num)))
print('O número {} tem a parte inteira {}. '.format(num, math.floor(num)))
print('O número {} tem a parte inteira {}. '.format(num, int(num)))
