#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoasMaiorPeso = list()
pessoasMenorPeso = list()
dados = []
totCadastro = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    totCadastro += 1
    if menor == 0:
        maior = dados[1]
        menor = dados[1]
    else:           #PROBLEMA PARA VERIFICAR O PESO!!!!
        for p in dados:
            if dados >= maior:
            maior = dados[1]
            pessoasMaiorPeso.append(dados[0])
        elif dados[1] <= menor:
            menor = dados[1]
            pessoasMenorPeso.append(dados[0])

    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print(f'Ao todo, você cadastrou {totCadastro} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de {pessoasMaiorPeso[0]}')
print(f'O menor peso foi de {menor}kg. Peso de {pessoasMenorPeso[0]}')