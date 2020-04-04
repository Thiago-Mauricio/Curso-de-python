'''Crie um programa que vai ler vários números e colocar em uma lista.
A)Quantos números foram digitados.
B)A lista de calores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

l = []
while True:
    l.append(int(input('Digite um número: ')))
    
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja continuar? [S/N] ').strip().upper()
    if stop == 'N':
        break
print(f'A quantidade de números digitados foi {len(l)}')
l.sort(reverse=True)
print(f'Os números digitados em ordem decrescente são: {l}')
if 5 in l:
    print('O número 5 está na lista.')
    #para saber o posição do 5 na lista, não foi pedido no exercicio
    #for p, a in enumerate(l):
        #if a == 5:
            #print(p)
else:
    print('O número 5 não foi digitado!')