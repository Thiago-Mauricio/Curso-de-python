'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverâ analisar se a expressão passada está abertos e fechados na ordem correta'''
exp = input('Digite uma expressão matemática: ')
a = []
for s in exp:
    if s == '(':
        a.append('(')
    elif s == ')':
        if len(a) > 0:
            a.pop()
        else:
            a.append(')')
if len(a) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida.')