import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print('O comprimento da \033[4mhipotenusa\033[m é: \033[1;32m{:.2f}\033[m' .format(hi))