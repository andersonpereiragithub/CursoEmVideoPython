#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#À vista dinheiro/cheque: 10% de desconto;
#Á vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('=' * 10, ' LOJAS GUANABAR ', '=' * 10 )

valor = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
pgto = int(input('[ 1 ] à vista dinheiro/cheque \n'
                 '[ 2 ] à vista cartão \n'
                 '[ 3 ] 2x no cartão \n'
                 '[ 4 ] 3x ou mais no cartão \n'
                 'Qual é a opção? '))

if pgto == 1:
    valorPgto = valor - (valor * 0.10)
elif pgto == 2:
    valorPgto = valor - (valor * 0.05)
elif pgto == 3:
    valorPgto = valor
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS' .format((valorPgto / 2)))
elif pgto == 4:
    valorPgto  = valor + (valor * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, (valorPgto / parcelas)))
else:
    print('\033[41mOpção INVÁLIDA!\033[m')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, valorPgto))


#MINHA SOLUÇÃO
# if pgto == 1:
#     print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.' .format(valor, valor - (valor * .10)))
# elif pgto == 2:
#     print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, valor - (valor * .05)))
# elif pgto == 3:
#     print('Sua compra vai custar R$ {:.2f} no final.'.format(valor))
# elif pgto == 4:
#     parcelas = int(input('Quantas parcelas? '))
#     print('Sua compra será parcelada em {}x de R$ {:.2f} com JUROS.'.format(parcelas, (valor + (valor * .20)) / parcelas))
#     print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, valor + (valor * .20)))
# else:
#     print('\033[41mOpção INVÁLIDA!\033[m')
