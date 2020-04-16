pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos' f'')
del pessoas['sexo']
pessoas['peso'] = 98.5
pessoas['nome'] = 'Leandro'
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(k, v)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
estado = dict()
brasil1 = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil1.append(estado.copy())
print(brasil1)
for e in brasil1:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil1:
    for v in e.values():
        print(v, end=' ')