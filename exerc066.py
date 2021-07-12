#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a Condição de Parada. No final, mostre quantos números
#foram digitados e qual foi a soma entre eles (desconsiderando o
#flag).
soma = cont = flag = 0
while True:
    flag = int(input('Digite um valor (999 para parar): '))
    if flag == 999: break
    soma += flag
    cont += 1

print(f'A soma dos {cont} valores foi {soma}!')