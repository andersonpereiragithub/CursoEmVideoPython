from exerc115.lib.interface import *
from exerc115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Deletar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('QUEM DESEJA DELETAR?')
        nome = str(input('Nome: '))
        deletarCadastro(arq, nome)
    elif resp == 4:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

