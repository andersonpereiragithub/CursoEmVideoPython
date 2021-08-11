#Crie um programa que tenha uma função fatorial() que receba
# dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.

def fatorial(num, show = False):
    """
    => Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Imprimir ou não a conta.
    :return: O valor do Fatorial de um número 'num'.
    """
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end = '')
            if c > 1:
                print(f' x ', end = '')
            else:
                print(f' = ', end = '')
        fat *= c
    return fat


print(fatorial(9, True))
help(fatorial)