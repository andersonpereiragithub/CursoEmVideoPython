#Escreva um programa que faça o computador "pensar" em um número
#inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual
#foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

numPc = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

numUsu = int(input('Qual número o PC escolheu? '))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
if numUsu == numPc:
    print('\033[32mPARABÉNS você VENCEU!\033[m')
else:
    print('\033[31mVocê PERDEU eu pensei em {} e não em {}\033[m!' .format(numPc, numUsu))

