def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: profavor, digite um número real válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31m Entrada de  dados cancelada pelo usuário!')
            return 0
        else:
            return num


num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor real: ')
print(f'O Valor inteiro digitado foi [{num1}] e o real foi [{num2}].')