#Faça um programa que leia 5 valores numéricos e guarde-os em
#uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e
#as sua respectivas posições na lista.
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digiver o {v + 1}º Valor: ')))
    if v == 0:
        menor = maior = v
    if v < menor:
        menor = v
    if v > maior:
        maior = v
print(f'Maior [ {maior} ]')
print(f'Menor [ {menor} ]')