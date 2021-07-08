#Escreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa. O programa vai perguntar o
#valor da casa, o salário da comprador e em quantos anos
#ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não
#exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Valor do Salário: R$ '))
anosPgto = int(input('Anos para pagamento: '))

valorPrestacao = valorCasa / (anosPgto * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos' .format(valorCasa, anosPgto))
print(' a prestação será de R$ {:.2f}' .format(valorPrestacao))

if valorPrestacao > (salario * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
