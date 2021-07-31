#Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('Crie', 'um', 'programa', 'que', 'tenha',
            'tupla', 'varias', 'palavras', 'depois',)
for str in palavras:
    print(f'\nNa palavra {str.upper()} temos ', end='')
    for letra in str:
        if letra.lower() in 'aeiou':
            print([ letra ], end=' ')