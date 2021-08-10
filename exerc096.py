# Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno retangular (largura e comprimento) e
# mostre a área do terreno.

def área(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c} m2.')


print('Contrelo de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
