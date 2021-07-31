#<<<<<<< HEAD
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
#=======
#Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
#cont9 = 0
#for n in range(0, 5):
#    numeros = (int(input(f'Digite [{n+1}/4]: ')))
#    if numeros == 9:
#        cont9 += 1
#print(f'O número 9 apareceu {cont9}\n'
#      f'A do primeiro valor 3 foi {numeros}')
#>>>>>>> 22eb8b02092cd09c896af2002da5ed70ff33d802
