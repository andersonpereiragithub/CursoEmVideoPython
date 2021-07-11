#Desenvolva um programa que leia o primeiro termo e a razão
#de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Informe o Primeiro Termo: '))
razao = int(input('Informe a razão da PA: '))
qntdeTermo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, qntdeTermo + razao, razao):
    print('{} ' .format(c), end='→ ')
print('ACABOU')