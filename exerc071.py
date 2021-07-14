#Crie um programa que simule o funcionamento de um caixa
# eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacasr? R$ '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed}  cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break

'''cedula = 50
contCiquenta = contVinte = contDez = contCinco = contUm = 0
saque = int(input('Valor a ser sacado: '))
totCed = 0


while saque > 0: # meu código
    while saque >= cedula:
        saque -= cedula
        contCiquenta += 1
    cedula = 20
    while saque >= cedula:
        saque -= cedula
        contVinte += 1
    cedula = 10
    while saque >= cedula:
        saque -= cedula
        contDez += 1
    cedula = 5
    while saque >= cedula:
        saque -= cedula
        contCinco += 1
    cedula = 1
    while saque >= cedula:
        saque -= cedula
        contUm += 1

print(f'[ {contCiquenta} ] notas de R$ 50,00;\n'
      f'[ {contVinte} ] notas de R$ 20,00;\n'
      f'[ {contDez} ] notas de R$ 10,00;\n'
      f'[ {contCinco} ] notas de R$  5,00;\n'
      f'[ {contUm} ] notas de R$  1,00;')'''