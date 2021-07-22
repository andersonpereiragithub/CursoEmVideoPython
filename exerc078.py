#Faça um programa que leia 5 valores numéricos e guarde-os em
#uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e
#as sua respectivas posições na lista.
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para posicão {v}: ')))
    if v == 0:
        menor = maior = valores[v]
    else:
        if valores[v] < menor:
            menor = valores[v]
        if valores[v] > maior:
            maior = valores[v]
print('-=' * 30)
print(f'Você digitou os valores {valores} ')
print(f'Maior valor é: [{maior}] nas posições', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f' [{pos}]...', end='')
print()
print(f'Menor valor é: [ {menor} ] nas posições', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f' [{pos}]...', end='')