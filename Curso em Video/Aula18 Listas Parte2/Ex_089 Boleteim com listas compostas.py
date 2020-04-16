'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
boletim = []
nome = []
nota = []
while True:
    no = input('Nome: ').upper().strip()
    nome.append(no)
    n = float(input('Nota 1: '))
    nota.append(n)
    n = float(input('Nota 2: '))
    nota.append(n)
    nome.append(nota[:])
    boletim.append(nome[:])
    nome.clear()
    nota.clear()
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja cadastrar mais alunos? [S/N] ').strip().upper()
    if stop == 'N':
        break
for c in range(0, len(boletim)):
    print(f'ALUNO: {boletim[c][0]:>10} | MÉDIA: {(boletim[c][1][0] + boletim[c][1][1]) / 2:>5}  | NOTAS: {boletim[c][1][0]:>5}   e {boletim[c][1][1]:>5}')