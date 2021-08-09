#Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols
# feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.
#===================================================================#

jogadores = dict()

jogadores['nome'] = str(input('Nome do Jogador: '))
qntdeJogo = int(input('Quantas partidas participou? '))
gols_jogos = []
somaGols = 0
for p in range(0, qntdeJogo):
    gols_jogos.append(int(input(f'Quantos gols fez na {p + 1}ª partida? ')))
    jogadores['totalGols'] = sum(p)
jogadores['gols'] = gols_jogos[:]
gols_jogos.clear()
print(jogadores)
