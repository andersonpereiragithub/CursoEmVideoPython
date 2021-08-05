#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.
notasAlunos = []
alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    notasAlunos.append([nome, [nota1, nota2], media])
    resp = str(input('Cadastrar outro? [S/N]'))
    if resp in 'Nn':
        break
print('-' * 25)
print(f'{"No.":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for pos, a in enumerate(notasAlunos):
    print(f'{pos:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(notasAlunos):
        print(f'Notas de {notasAlunos[opc][0]} {notasAlunos[opc][1]}')
print('<<< VOLTE SEMPRE >>>')