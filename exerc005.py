# Desafio 5
num = int (input('Inserir número: '))
print("Antecessor de {} é = {}" .format(num, num - 1))
print('Sucessor de {} é = {}' .format(num, num + 1))

# Desafio 6
print('O dobro de {} é = {}' .format(num, (num * 2)))
print('O triplo de {} é = {}' .format(num, (num * 3)))
print('O raíz quadrada de {} é = {}' .format(num, (num ** (1/2))))

# Desafio 7
n1 = float(input("1º Noata: "))
n2 = float(input("2º Noata: "))
m = (n1 + n2) / 2
print('A média das notas é: ', m)

# Desafio 8
num2 = float(input('Metros: '))
print('{0} metros são {1} centímetros.' .format(num2, num2*100))
print('{0} metros são {1} milímetros.' .format(num2, num2*1000))

# Desafio 9
num3 = int(input('Inserir um número: '))
print('*' * 12)
print(' {} x {:2} = {}' .format(num3, 1, num3 * 1))
print(' {} x {:2} = {}' .format(num3, 2, num3 * 2))
print(' {} x {:2} = {}' .format(num3, 3, num3 * 3))
print(' {} x {:2} = {}' .format(num3, 4, num3 * 4))
print(' {} x {:2} = {}' .format(num3, 5, num3 * 5))
print(' {} x {:2} = {}' .format(num3, 6, num3 * 6))
print(' {} x {:2} = {}' .format(num3, 7, num3 * 7))
print(' {} x {:2} = {}' .format(num3, 8, num3 * 8))
print(' {} x {:2} = {}' .format(num3, 9, num3 * 9))
print(' {} x {:2} = {}' .format(num3, 10, num3 * 10))
print('*' * 12)

# Desafio 10
num4 = float(input('Valor em Reais R$ '))
print('Valor em dólares $ {:1f}' .format(num4/3.27))

# Desafio 11
altura = float(input('Altura: '))
largura = float(input('Largura: '))
print('Area = ', altura * largura)
print('{} litros para pintar' .format((altura * largura) / 2))

# Desafio 12
num5 = float(input('Preço: '))
print('Preço com 5% de desconto é: {:.2f}'.format(num5 * 0.95))

# Desafio 13
num6 = float(input('Salário: '))
print('Com 15% de aumento é: R$ {:.2f}'.format(num6 + (num6 * 0.15)))