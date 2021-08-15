from exerc115.lib.interface import *


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


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


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