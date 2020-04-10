'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostra o contéudo da estrutura na tela'''


aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
while aluno['Média'] < 0 or aluno['Média'] > 10:
    aluno['Média'] = float(input('A média precisa estar entre 0 e 10, digite novamente: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7 :
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')