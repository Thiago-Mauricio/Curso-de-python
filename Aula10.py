#parte teórica:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo!!!')
else:
    print('Carro velho!!!')
print('--FIM--')

#Condição simplificada
print(f'Carro novo !!!' if tempo <= 3 else 'Carro velho')
print('FIM !!!!')

#Parte prática:
nome = str(input('Qual o seu nome? '))
if nome == 'Thiago':
    print('Que nome lindo você tem !!!')
print(f'Bom dia {nome}')