#Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint

print('-' * 30)
print(f'      JOGA NA MEGA SENA     ')
print('-' * 30)

qtdNum = int(input('Quantos jogos serão gerados? '))
lista = []
num = randint(1, 60)