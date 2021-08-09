# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dict_pessoas = dict()
lista_dados = []
soma = media = 0
while True:
    dict_pessoas['nome'] = str(input('Nome: '))
    while True:
        dict_pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dict_pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    dict_pessoas['idade'] = int(input('Idade: '))
    soma += dict_pessoas['idade']
    lista_dados.append(dict_pessoas.copy())
    while True:
        resp = str(input('Deseja cadastrar outra? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp  == 'N':
        break
print('-=' * 20)
print(f'A) Foram cadastradas {len(lista_dados)} pessoas.')
media = soma / len(lista_dados)
print(f'B) A média de idade é de [{media:5.2f}] anos.')
print(f'C) As mulheres cadastradas foram ', end = '')
for p in lista_dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print(f'As pessoas com idade acima da média são: ')
for p in lista_dados:
    if p['idade'] >= media:
        print(f'     ', end = ' ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<< ENCERRADO >>>')
