#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dadosTemp = []
dadosPrincipais = []
maior = menor = 0
while True:
    dadosTemp.append(str(input('Nome: ')))
    dadosTemp.append(float(input('Peso: ')))
    if menor == 0:
        maior = menor = dadosTemp[1]
    else:
        if dadosTemp[1] > maior:
            maior = dadosTemp[1]
        elif dadosTemp[1] < menor:
            menor = dadosTemp[1]
    dadosPrincipais.append(dadosTemp[:])
    dadosTemp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 25)
print(f'Ao todo, você cadastrou {len(dadosPrincipais)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in dadosPrincipais:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de', end='')
for p in dadosPrincipais:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')