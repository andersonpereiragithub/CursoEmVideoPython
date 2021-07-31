#Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:
    num = int(input('Informe valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
            print('Valor Duplicado! Não vou adicionar...')
    r = str(input('Deseja inserir outro numero [N/S]? ')).strip().upper()
    if r == "N":
        break
valores.sort()
print('-=' * 25)
print(f"Os valore digitados foram {valores}")