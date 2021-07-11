#Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

certo = False
sexo = str(input('Informe seu Sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos! Informe seu Sexo (M/F): ')).strip().upper()[0]

print('Sexo {} Cadastrado com sucesso!' .format(sexo))
