#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

import random
from time import sleep

numPc = random.randint(0, 11)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
cont = 0
while acertou == False:
    numUsu = int(input('Qual número o PC escolheu? '))
    print('\033[33mPROCESSANDO...\033[m')
    sleep(1)
    cont += 1
    if numUsu == numPc:
        acertou = True
    else:
        if numPc < numUsu:
            print('Menos')
        else:
            print('Mais')

print('\033[32mPARABÉNS você VENCEU com {} tentativas!\033[m' .format(cont))
