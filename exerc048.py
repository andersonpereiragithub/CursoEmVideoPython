#Faça um programa que calcule a soma entre todos os números ímpares que
#são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
count = 0
for c in range(1, 501, 2): #O 2 faz a leitura dos ímpares, pois partindo do 1 vai de 2 em 2.
    if c % 3 == 0:
        soma += c
        count += 1
print('A soma de todos os {} valores solicitados é {}' .format(count, soma))