#Crie um programa que faça o computador jogar JOKENPÔ
#com você. (Jogo do papel, pedra e tesoura)
import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Sua opções:''')

jogador = int(input('Escolha uma opção abaixo \n'
                   '[ 0 ] Pedra\n'
                   '[ 1 ] Papel \n'
                   '[ 2 ] Tesoura \n'
                    'Opção: '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
sleep(1)

print('-=' * 12)
print('Computador escolheu [ {} ] \n'
      'Jogador escolheu [ {} ]' .format(itens[computador], itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador VENCEU!')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Venceu!')
    else:
        print('Jogada Inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu!')
    elif jogador == 1:
        print('Computador Vendeu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')
