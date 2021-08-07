#Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols
# feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.

statusJogador = {}
partidas = []
statusJogador['nome'] = str(input('Nome do jogador: '))
qntde_Partidas = int(input(f'Quantas partidas {statusJogador["nome"]} jogou? '))
for c in range(0, qntde_Partidas):
    partidas.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
statusJogador['gols'] = partidas[:]
statusJogador['total_gols'] = sum(partidas)
print('-=' *20)
print(statusJogador)
print('-=' *20)
for k, v in statusJogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' *20)
print(f'O jogador {statusJogador["nome"]} participou de {len(statusJogador["gols"])} jogos.')
for i, v in enumerate(statusJogador['gols']):
    print(f'    => Na partida {i + 1}ª, fez {v} gols')
print(f'Foi um total de {statusJogador["total_gols"]} gols')