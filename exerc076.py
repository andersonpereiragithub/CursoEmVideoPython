#Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência. No
# final, mostre uma listagem de preços, organizando os
# dados em forma tabular.
produtos = ('Caderno', 15.90,
            'Borracha', 1.50,
            'Caneta', 3.00,
            'Computador', 1300.00,
            'Lápis', 1.00,
            'Chocolate 1kg', 500,
            'Livro', 34.90,
            'Mochila', 120.32)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-' * 40)