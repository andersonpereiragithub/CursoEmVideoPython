from exerc115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Lista de pessoas cadastradas', 'Ordenar por nome', 'Ordenar por idade(não funcionando)', 'Cadastrar nova Pessoa', 'Deletar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        lista(arq)
    elif resp == 2:
        lista(arq, 1)
    elif resp == 3:
        lista(arq, 2)
    elif resp == 4:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 5:
        cabecalho('QUEM DESEJA DELETAR?')
        nome = str(input('Nome: '))
        deletarCadastro(arq, nome)
    elif resp == 0:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

