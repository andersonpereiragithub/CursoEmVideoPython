# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = numPro = menor = 0
nome = nomeB = ' '
while True:
    nome = str(input('Nome: '))
    preco = float(input('Preço: '))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    if menor == 0:
        menor = preco
    else:
        if preco < menor:
            nomeB = nome
    if preco > 1000:
        numPro += 1
    if resp != 'S':
        break
print(f'Total gasto na compra foi [ {soma} ].\n'
      f'Produtos que custam mais de R$ 1000 são [ {numPro} ].\n'
      f'O nome do produto mais barato é [ {nomeB} ]')