#Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = qntde = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qntde += 1
    if qntde == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
print('Você digitou {} númeors e a média foi = {} \n'
      'O valor Maior = {} \n'
      'O Valor Menor = {}' .format(qntde, soma / qntde, maior, menor))