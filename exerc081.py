# Crie um programa que vai ler vários números e
# colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numLista = []

while True:
    numLista.append(int(input('Número: ')))
    resp = input('Deseja continuar [S/N]? ')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(numLista)} números.')
numLista.sort(reverse=True)
print(f'A lista de números decrescente é: {numLista}')
if 5 in numLista:
    print('O número 5 está na lista.')
else:
    print('O número 5 NÃO está na lista.')
