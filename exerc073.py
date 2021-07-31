# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

#Pesquisar Tabelagi

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético Mineiro',
         'Botafogo', 'Atlético Paranaense', 'Bahia', 'São Paulo', 'Fluminense',
         'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goiano' )

print('-=' * 30)
print(f'Lista de times do Brasileirão:\n {times}')
print('-=' * 30)

print('-=' * 30)
print(f'OS 5 primeiros são:\n {times[0:5]}')
print('-=' * 30)

print('-=' * 30)
print(f'OS 4 últimos são:\n {times[-4:]}')
print('-=' * 30)

print('-=' * 30)
print(f'Times em ordem alfabética:\n {sorted(times)}')
print('-=' * 30)

print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
print('-=' * 30)