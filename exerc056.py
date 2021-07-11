#Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, mostre: a média
# de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

somaIdade = 0
idadeHomeMaisVelho = 0
nomeHomeMaisVelho = ''
mulheresMenosVinte = 0

for p in range(1, 5):
    print('-' * 5, ' {}ª PESSOA ' .format(p), '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): '))
    somaIdade += idade
    if sexo == 'M':
        if idade > idadeHomeMaisVelho:
            idadeHomeMaisVelho = idade
            nomeHomeMaisVelho = nome
    elif sexo == 'F' and idade < 20:
        mulheresMenosVinte += 1

print('A Média idade do grupo é de: {} anos.' .format(somaIdade / 4))
print('O Homem mais velho tem {} anos e se chama: {}' .format(idadeHomeMaisVelho, nomeHomeMaisVelho))
print('Ao todo são {} mulher(es) tem menos de 20 anos' .format(mulheresMenosVinte))