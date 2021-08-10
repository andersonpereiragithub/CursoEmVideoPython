#Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’)
# Saída: ~~~~~~~~~
#        Olá, Mundo!
#        ~~~~~~~~~

def escreva(str):
    num = len(str) + 4
    print(f'~' * num, f'\n  {str}\n',f'~' * num)


frase = str(input('Escreve uma mensagem: '))
escreva(frase)
