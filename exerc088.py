#Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from  time import sleep
print('-' * 30)
print(f'      JOGA NA MEGA SENA     ')
print('-' * 30)
lista = []
listaFinal = []
qtdeNum = 1 + int(input('Quantos jogos serão gerados? '))
tot = 0
for n in range(1, qtdeNum):
    while tot < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            tot += 1
    lista.sort()
    listaFinal.append(lista[:])
    lista.clear()
    tot = 0
for pos, l in enumerate(listaFinal):
    print(f'Jogo nº {pos + 1}: {l}')
    sleep(1)