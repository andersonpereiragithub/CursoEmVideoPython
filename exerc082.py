#Crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numLista = []
listaPar = []
listaImpar = []

while True:
    numLista.append(int(input('Insira uma valor: ')))
    resp = input('Deseja continuar [S/N]? ')
    if resp in 'Nn':
        break

for pos, v in enumerate((numLista)):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)
print('-=' * 30)
print(f'Lista com todos números: {numLista}\n'
      f'Lista com todos números Pares: {listaPar}\n'
      f'Lista com todos números Ímpares: {listaImpar}\n')