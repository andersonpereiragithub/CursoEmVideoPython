#Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print(f'O valor 9 apareceu {valores.count(9)} vezes.\n'
      f'O valor 3 foi digitana na {valores.index(3) + 1}º posição.\n'
      f'Os valores pares foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end =' ')