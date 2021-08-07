#Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dadosAluno = {}
nomeAluno = str(input('Nome: '))
mediaAluno = float(input(f'Média de {nomeAluno}: '))
print('-=' * 20)
situacao = ' '
if mediaAluno < 7:
    situacaoAluno = 'REPROVADO'
else:
    situacaoAluno = 'APROVADO'
dadosAluno = {f'nome': nomeAluno, 'media': mediaAluno, 'situacao': situacaoAluno }

for k, a in dadosAluno.items():
    print(f'- {k} é igual a {a}' )

