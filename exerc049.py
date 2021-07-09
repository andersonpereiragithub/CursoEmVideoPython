#Mesma Tabuada do Desfio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Escolha um número para ver a Tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {:2}' .format(num, c, num * c))