#Escreva um programa que leia um número inteiro qualque
# e peça para o usuário escolher qual será a base de conversão:
#1 para Binário, 2 para Octal, 3 para Hexadecimal

num = int(input('Informe um número: '))

escolha = int(input('Escolha a Conversão, \n (1) Binário \n (2) Octal \n (3) Hexadecimal \n Sua Opção: '))

if escolha == 1:
    print('{} Binario é: {}' .format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} Octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Oção inválida. Tente Novamente.')