#Desenvolva um programa que pergunte a distância em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km
#para viagens de até 200Km e  R$ 0,45 para viagens mais
#longas.

distancia = int(input('Qual a distância da viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
valor = distancia * 0.45
print('O valor cobrado é de R$ {:.2f}' .format(valor))