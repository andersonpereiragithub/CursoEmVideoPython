#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

contMaior = contHomens = contMulheres =0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if idade > 18:
        contMaior +=1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheres += 1
    if resp != 'S':
        break

print(f'[ {contMaior} ] Pessoas tem mais de 18 anos.'
      f'\n[ {contHomens} ] Homens foram cadastrados.'
      f'\n[ {contMulheres} ] Mulheres tem menos de 20 anos.')