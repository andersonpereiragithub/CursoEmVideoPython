#Escreva um programa que converta uma temperatura
#digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura em ºC: '))
print('A tempera de {} ºC é de {} ºF.' .format(c, ((c*9)/5) + 32))