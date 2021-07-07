#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome.

nomeCompleto = str(input('Digite um nome completo: ').strip()) #para cortar espaços antes e depois
print('Seu nome em maiúsculas é {}. ' .format(nomeCompleto.upper()))
print('Seu nome em minúsculas é {}. ' .format(nomeCompleto.lower()))
print('Seu nome tem {} letras' .format(len(nomeCompleto) - nomeCompleto.count(' ')))
print('Seu primeiro nome tem {} letra' .format(nomeCompleto.find(' ')))
separaNome = nomeCompleto.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separaNome[0], len(separaNome[0])))