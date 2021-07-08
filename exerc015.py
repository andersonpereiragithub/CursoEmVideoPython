dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

print('O total a pagar é de R$ {:.2f}.' .format(dias * 60.0 + km * 0.15))