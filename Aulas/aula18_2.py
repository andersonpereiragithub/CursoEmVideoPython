#Lista Compostas
#

teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
print(galera)
print(len(galera))
print('-=' * 30)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(len(galera))
print('-=' * 30)

galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 12], ['Maira', 45]]
print(galera[0])
print(galera[0][0])
print('-=' * 30)

print(galera[2][1])
print('-=' * 30)

for p in galera:
    print(p)
print('-=' * 30)

for p in galera:
    print(p[0])
print('-=' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-=' * 30)

pessoas = list()
dados = list()
for c in  range(0, 2):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)
print('-=' * 30)
totmaior = totmenor = 0
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maior(es) e {totmenor} menor(es) de idade.')