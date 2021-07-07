#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza Primeiro = Ana Último = Souza

nomeCompleto = input('Digite o nome Completo: ')
separado = nomeCompleto.split(' ')
print('Primeiro = {} \n Último = {}'.format(separado[0], separado[len(separado)-1]))