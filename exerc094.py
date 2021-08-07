# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = []
dict_pessoas = dict()
lista_dados = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Sexo [M/F]: ')))
    pessoa.append(int(input('Idade: ')))
    dict_pessoas = pessoa[:]
    pessoa.clear()
    lista_dados.append(dict_pessoas)
    resp = str(input('Deseja cadastrar outra? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(lista_dados)} pessoas.')
print()