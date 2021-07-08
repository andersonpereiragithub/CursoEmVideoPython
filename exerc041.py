#A Confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
#Até 9 anos : Mirim
#Até 14 anos: INFANTIL
#Até 17 anos: JÚNIOR
#Até 20 anos: Sênior
#Acima: MASTER
import datetime

nascimento = int(input('Ano nascimento: '))

idade = int(datetime.datetime.today().year) - nascimento

if idade <= 9:
    print('Categoria \033[41mMIRIM\033[m com {} de idade.' .format(idade))
elif idade <= 14:
    print('Categoria \033[41mINFANTIL\033[m com {} de idade.' .format(idade))
elif idade <= 19:
    print('Categoria \033[41mJÚNIOR\033[m com {} de idade.' .format(idade))
elif idade <= 25:
    print('Categoria \033[41mSÊNIOR\033[m com {} de idade.'.format(idade))
else:
    print('Categoria \033[41mMASTER\033[m com {} de idade.'.format(idade))
