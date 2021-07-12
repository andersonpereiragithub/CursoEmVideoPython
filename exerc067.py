#Faça um programa que mostre a tabuada de vários números, um
# de cada vez, para cada valor digitado pelo usuário. O programa
# será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Gerar Tabuada de: '))
    print('-' * 11)
    if num < 0:
        break

    for c in range(1, 11):
        print(f'{num} x {c:2} = {c * num:2}')
    print('-' * 11)
print('Fim!')