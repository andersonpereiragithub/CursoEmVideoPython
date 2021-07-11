#Faça um programa que leia o peso de cinco pessoas. No final,
#mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('Informe o Peso da {}a. pessoa (Kg): '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('Maior peso é {}Kg \nMenor peso é {}Kg ' .format(maior, menor))