# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    flag = n
    soma += n
    n = int(input('Digite um número: '))
print('Foram digitados {} números e a soma é [{}]'.format(cont, soma))