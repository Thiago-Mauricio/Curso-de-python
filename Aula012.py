nome = input('Qual é o seu nome? ')
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino você tem!')
else:
    print('Seu nome é uma bosta!')
print(f'Tenha um bom dia {nome}')