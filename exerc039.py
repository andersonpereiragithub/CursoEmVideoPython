#Faça um progra que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço Militar;
#Se é a hora de se alistar;
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

anoAtual = datetime.date.today().year
anoNascimento = int(input('Informe Ano Nascimento: '))

if (anoAtual - anoNascimento) < 18:
    print('Ainda falta(m) {} ano(s) para se alistar!' .format(18 - (anoAtual - anoNascimento)))
    print('O alistamento deverá ser feito em {}.' .format((anoAtual + 18) - (anoAtual - anoNascimento)))
elif (anoAtual - anoNascimento) == 18:
    print('É ano de se alistar.')
else:
    print('Já passou {} ano do seu alistamento.' .format((anoAtual - anoNascimento) - 18))
    print('O alistamento deveria ser feito em {}.'.format((anoAtual + 18) - (anoAtual - anoNascimento)))
