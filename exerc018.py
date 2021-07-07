import math
teste = '\033[m'
num = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de \033[47m{:.2f}\033[m tem o \033[4mSENO\033[m de {:.2f}' .format(num, math.sin(math.radians(num))))
print('O ângulo de \033[47m{:.2f}\033[m tem o \033[4mCOSSENO\033[m de {:.2f}' .format(num, math.cos(math.radians(num))))
print('O ângulo de \033[47m{:.2f}\033[m tem A \033[4mTANGENTE\033[m de {:.2f}' .format(num, math.tan(math.radians(num))))
