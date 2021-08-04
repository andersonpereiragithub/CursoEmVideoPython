#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digete valor na posição[{l},{c}]: '))
print('-=' * 20)
somaPar = 0
somaColuna3 = 0
maior = matriz[1][0]
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaColuna3 += matriz[l][c]
        if maior < matriz[1][c]:
            maior = matriz[1][c]
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()
print('-=' * 20)
print(f'A soma de todos os Pares é: [{somaPar}]')
print(f'A soma dos valores da terceira coluna é: [{somaColuna3}]')
print(f'O maior valor da segunda linha é: [{maior}]')

