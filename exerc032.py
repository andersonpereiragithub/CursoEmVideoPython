#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Informe um ano para saber se é Bissexto: '))
if(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano {} é Bissexto!'.format(ano))
else:
    print('Ano {} NÃO é Bissexto'.format(ano))