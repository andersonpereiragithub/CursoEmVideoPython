#Refaça o DESAFIO 51, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
cont = 1

while cont <= 10:
    print('{} ' .format(termo), end='→ ')
    termo += razao
    cont += 1
print('FIM!!!')