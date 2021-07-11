#Crie um programa que leia uma frase qualquer e diga se ela é um
#palíndromo, desconsiderando os espaços. Exemplos: APOS A SOPA,
#A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ' '
inverso = junto[::-1]

'''for letra in range(len(junto) - 1, -1, -1): # inverter a palavra
    inverso += junto[letra]'''

print('O inverso de [{}] é [{}].'.format(frase, inverso))

if inverso == junto:
    print('Temos um PALÍNDROMO! [{}]' .format(inverso))
else:
    print('A frase digitada não é um Palíndromo.')