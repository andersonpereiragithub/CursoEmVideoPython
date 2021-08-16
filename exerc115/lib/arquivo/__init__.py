from exerc115.lib.interface import *
from operator import itemgetter


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print(f'Novo registro de {nome} adicionado.')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
            a.close()


def verificaCadastro(arq, pessoa):
    a = open(arq, 'r')
    p = False
    for valor in a:
        n = valor.split(';')
        if pessoa == n[0]:
            p = True
    return p


def deletarCadastro(arq, pessoa):
    existe = verificaCadastro(arq, pessoa)
    if existe:
        a = open(arq, 'r')
        lista = []
        for valor in a:
            n = valor.split(';')
            if n[0] != pessoa:
                lista.append(valor)
        a.close()
        b = open(arq, 'w')
        for v in lista:
            b.write(f'{v}')
        b.close()
        print(f'{pessoa} deletada com sucesso!')
    else:
        print(f'{pessoa} não encontrada!')


def lista(arq, ordenado=0):
    linhas = open(arq, 'r')
    dictPessoas = {}
    listaPessoas = []
    for lin in linhas:
        dado = lin.split(';')
        dictPessoas['nome'] = dado[0]
        dictPessoas['idade'] = dado[1].replace('\n', '')
        listaPessoas.append(dictPessoas.copy())
        dictPessoas.clear()
    linhas.close()
    if ordenado == 1:
        lista = sorted(listaPessoas, key=itemgetter('nome'))
        lerArquivo(lista)
    elif ordenado == 2:
        lista = sorted(listaPessoas, key=itemgetter('idade'))
        lerArquivo(lista)
    else:
        lerArquivo(listaPessoas)


def lerArquivo(lista):
    cabecalho(f'LISTA DAS {len(lista)} PESSOAS CADASTRADAS')
    for dado in lista:
        print(f'{dado["nome"]:<30}{dado["idade"]:>3} anos')