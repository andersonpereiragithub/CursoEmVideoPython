#Melhore o DESAFIO 61, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.



print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
cont = 1
nQtde = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        if nQtde == 0:
            print('{} ' .format(termo), end='→ ')
            termo += razao
            cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))