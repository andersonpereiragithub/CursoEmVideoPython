#Faça um progra que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço Militar;
#Se é a hora de se alistar;
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

anoNascimento = int(input('Informe Ano Nascimento: '))

if (anoNascimento - datetime.date.year) < 18:
    print('Ainda falta {} meses para se alistar!' .format((anoNascimento - datetime.date.year) - 18))
elif anoNascimento - datetime.date.year == 18:
    print('É a hora de se alistar.')
else:
    print('Já passou {} tempo do alistamento' .format(anoNascimento - datetime.date.year))
