#Crie um programa que leia dois valores e mostre um
# menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
num1 = float(input('Primeiro Valor: '))
num2 = float(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('[ 1 ] somar \n'
                      '[ 2 ] multiplicar\n'
                      '[ 3 ] maior\n'
                      '[ 4 ] novos números\n'
                      '[ 5 ] sair do programa\n'
                      '>>>>> Qua é a sua opção? '))
    if opcao == 1:
        print('Soma de {} + {} = {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('Multiplicação de {} + {} = {},'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o {} é o Maior!'.format(num2, num1, maior))
    elif opcao == 4:
        num1 = float(input('Primeiro Valor:: '))
        num2 = float(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida!')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa! Volte sempre!')
