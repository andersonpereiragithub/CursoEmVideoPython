#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo
#que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.

velo = int(input('Qual a velocidade do carro? '))
if velo > 80:
    print('Você foi multado!')
    valorMulta = (velo - 80) * 7.00
    print('Valor da multa é de R$ {:.2f}'.format(valorMulta))
print('Dentro da velocidade permitida!')
