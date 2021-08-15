def lerArquivo(file):
    try:
        a = open(file, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def ordernarArquivo(arq):
    linhas = open(arq, 'r')
    dictPessoas = []
    listaPessoas = []
    for linha in linhas:
        dado = linha.split(';')
        dictPessoas.append(dado[0])
        dictPessoas.append(dado[1])
        listaPessoas.append(dictPessoas[:])
        dictPessoas.clear()
    listaPessoas.sort()
    linhas.close()
    linhas = open(arq, 'w')
    for v in listaPessoas:
        linhas.write(f'{v[0]};{v[1]}')
    linhas.close()
    lerArquivo(linhas)


arq = 'cursoemvideo.txt'
ordernarArquivo(arq)