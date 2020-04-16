import random
#com shuffle:
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f"A ordem de apresentação será: {lista}.")
lista = random.sample([n1, n2, n3, n4],k=4)
print(f'A ordem será: {lista} ')
lista = random.choices([n1, n2, n3, n4], k=5)
print(f'A ordem será: {lista}')

#com sample: pode escolher quantidade de sorteados, não repetindo resultados, trava se o numero em K for maior que o banco de dados
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = random.sample([a1, a2, a3, a4],k=4)
print(f'A ordem será: {alunos} ')

#com choices: pode escolher quantidade de sorteados, porém pode repetir um mesmo sorteado. Não trava se o numero em K for maior que o banco de daods
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
ordem = random.choices([al1, al2, al3, al4], k=3)
print(f'A ordem será: {ordem}')