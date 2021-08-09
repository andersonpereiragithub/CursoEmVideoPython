#Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols
# feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.
#===================================================================#
time = list()
jogadores = dict()
gols_jogos = []
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do Jogador: '))
    qntdeJogos = int(input('Quantas partidas participou? '))
    gols_jogos.clear()
    for c in range(0, qntdeJogos):
        gols_jogos.append(int(input(f'   Quantos gols fez na {c + 1}ª partida? ')))
    jogadores['gols'] = gols_jogos[:]
    jogadores['totalGols'] = sum(gols_jogos)
    time.append(jogadores.copy())
    while True:
        resp = str(input('Cadastrou outor? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-' * 30)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end = '')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No {i + 1}º jogo fez {g} gols.')
    print('-' * 45)
print('<< volte sempe >>')