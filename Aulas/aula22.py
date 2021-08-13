#Nessa aula, vamos continuar nossos estudos de funções em Python,
# aprendendo como criar módulos em Python e reutilizar nossos
# códigos em outros projetos. Vamos aprender também como agrupar
# vários módulos em um pacote, ampliando ainda mais a modularização
# em grandes projetos em Python.
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatoria de {num} é {fat}.')