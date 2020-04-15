'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O Programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido fornecido'''

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Nome do Jogador: ').strip()
g = input('Número de gols: ').strip()
print(ficha(n, g))
