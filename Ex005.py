# Maneira como fiz:
m = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {} e o seu sucessor é {}'.format(m, m - 1, m + 1))

#método do professor:
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

#atualização do .format:
x= int(input('Digite um numero: '))
#F é colocado antes das aspas sem espaço e as variaveis dentro das chaves
print(f'Atencessor de {x} é {x-1}, e o seu sucessor é {x+1}')