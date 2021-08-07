#Dicionários são representados por { }

pessoas = {'nome': 'Delon', 'idade': 48, 'sexo': 'M', 'peso': 98.3}
print(f'{pessoas["nome"]} tem {pessoas["idade"]}, é do sexo {pessoas["sexo"]} e pesa {pessoas["peso"]}Kg.')
print('-' * 50)
print(pessoas)
print('-' * 50)
print(pessoas.keys())
print('-' * 50)
print(pessoas.values())
print('-' * 50)
print(pessoas.items())
print('-' * 50)
for k, v in pessoas.items():
    print(f'{k}: {v:^10}')
print('-' * 50)
estado = dict() #estado = {}
brasil = list() #brasil = []
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print('-' * 50)
for e in brasil:
    print(e)
print('-' * 50)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
print('-' * 50)