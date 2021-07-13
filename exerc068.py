#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
import random

print('=' * 20)
print('Jogo do PAR ou ÍMPAR')
print('=' * 20)

while True:
    num = int(input('Escolha um número: '))
    tipo = str(input('Par ou Ímpar [P/I]? ')).upper().strip()
    if tipo == 'P':
        tipo = 'PAR'
    else:
        tipo = 'ÍMPAR'
    computador = random.randint(1, 10)
    resultado = num + computador
    if resultado % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'

    print(f'Você escolheu [{num}]\nComputador escolheu [{computador}]\n Você pediu {tipo}')

    print('~' * 18)
    print(f'Resultado foi [ {res} ]!')
    if tipo == res:
        print('Você VENCEU!')
    else:
        print('Computador VENCEU!')
        break
    print('~' * 18)