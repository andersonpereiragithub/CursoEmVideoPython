def aumentar(preco=0 , taxa=0, formato=False):
    """
    --> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem de aumento.
    :param formato: quer a saída formatada ou não?
    :return:o valor reajustado, com ou sem formato.
    """
    resp = preco + (preco * taxa / 100)
    return resp if formato is False else moeda(resp)


def diminuir(preco=0, taxa=5, formato=False):
    resp = preco - (preco * taxa / 100)
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    resp = preco * 2
    return resp if not formato else moeda(resp)


def metade(preco=0, formato=False):
    resp = preco / 2
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='RS'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t[{moeda(preco)}]')
    print(f'Dobro do preço: \t[{dobro(preco, True)}]')
    print(f'Metade do preço: \t[{metade(preco, True)}]')
    print(f'{taxaa}% de aumento: \t[{aumentar(preco, taxaa, True)}]')
    print(f'{taxar:2}% de redução: \t[{diminuir(preco, taxar, True)}]')
    print('-' * 30)