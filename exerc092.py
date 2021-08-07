#Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
trabalhadores = {}
trabalhadores['nome'] = str(input('nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
trabalhadores['idade'] = datetime.now().year - anoNascimento
trabalhadores['carteiraTrabalho'] = int(input('Número CTPS (0 não tem): '))
if trabalhadores['carteiraTrabalho'] != 0:
    anoContr = int(input('Ano Contratação: '))
    trabalhadores['anoContratacao'] = anoContr
    trabalhadores['salario'] = float(input('Salário: '))
    trabalhadores['anoAposentadoria'] = trabalhadores['idade'] + ((trabalhadores['anoContratacao'] + 35) - datetime.now().year)
print('-=' * 20)
for k, v in trabalhadores.items():
    print(f' - {k} tem valor {v}')
