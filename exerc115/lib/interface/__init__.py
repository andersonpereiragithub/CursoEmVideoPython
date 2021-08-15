def leiaInt(msg):
    """
    --> Valida se o dado informado "msg" é um número inteiro.
    :param msg: valor a ser validado.
    :return: 0 se aplicação for interrompida pelo usuário ou "num" se inteiro válido.
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('= MENU PRINCIPAL =')
    c = 1
    for item in lista:
        if c == len(lista):
            print(f'\033[33m{0}\033[m - \033[34m{item}\033[m')
        else:
            print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc