#Escreva um programa que pergunta o salário de um funcionário
#e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento
#de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salário: '))
if salario > 1250.00:
    salario += salario * 0.10
else:
    salario += salario * 0.15

print('O salário com aumento é de R$ {:.2f}'.format(salario))