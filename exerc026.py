#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra [ A ] aparece {} vezess' .format(frase.upper().count('A')))
print('A letra [ A ] aparece na posição {}.' .format(frase.find('A')+1))
print('A letra [ A ] aparece na última posição {}.' .format(frase.rfind('A')+1))
print('Existem {} letras nesta frase.' .format(len(frase)-frase.count(' ')))