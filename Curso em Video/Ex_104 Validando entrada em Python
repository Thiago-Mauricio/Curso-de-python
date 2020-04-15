'''Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas valor numérico.'''

def leiaint(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            break
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return valor

        

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')