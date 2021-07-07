#Crie um programa que leia o nome de uma pessoa e diga se ela tem
#"SILVA" no nome.

nome = str(input('Digite um nome: ')).strip()
print('O nome digitado tem SILVA? {}' .format('silva' in nome.lower()))