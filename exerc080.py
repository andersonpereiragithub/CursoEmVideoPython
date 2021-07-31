# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

valores = []
for c in range(0, 5):
    num = int(input('Informe valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado no final dos Valores...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adicionado na posição {pos} dos Valores...')
                break
            pos += 1
print('-=' * 21)
print(f"Os valore digitados foram {valores}")