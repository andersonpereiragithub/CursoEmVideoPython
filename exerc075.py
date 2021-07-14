#Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
cont9 = 0
for n in range(0, 5):
    numeros = (int(input(f'Digite [{n+1}/4]: ')))
    if numeros == 9:
        cont9 += 1
print(f'O número 9 apareceu {cont9}\n'
      f'A do primeiro valor 3 foi {numeros}')