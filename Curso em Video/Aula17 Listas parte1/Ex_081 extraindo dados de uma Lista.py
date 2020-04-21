'''Crie um programa que vai ler vários números e colocar em uma lista.
A) Quantos números foram digitados.
B) A lista de calores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    while True:
        try:
            lista.append(int(input('Digite um número inteiro: ')))
            break
        except:
            print('Erro: O campo deve ser preenchido com um númeor inteiro')
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
print(f'Foram digitados {len(lista)} números')
print(f'Os números digitados foram {sorted(lista)}')
if 5 in lista:
    print (f'O valor 5 foi digitado na posição {lista.index(5)}')
else:
    print(f'O valor 5 não foi digitado na lista')
