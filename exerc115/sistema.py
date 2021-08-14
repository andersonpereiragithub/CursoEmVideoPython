from exerc115.lib.interface import *
from time import sleep

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        print('')
    elif resp == 2:
        print('')
    elif resp == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

