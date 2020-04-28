from random import randint
print(randint(10, 121))

def aluguel(dias, km):
    total = (dias * 60) + (km * 0.15)
    print(f'O valor total a ser pago é de R$: {total:.2f}')


print('=' * 40)
print('{:^40}'.format('Aluguel de Carros.'))
print('=' * 40)
while True:
    while True:   
        try:
            dias = int(input('Por quantos dias o carro foi alugado? '))
            break
        except:
            print('Erro: digite apenas números inteiros! ')
    print('-' * 40)
    while True:
        try:
            km = float(input('Quantos Kms foram percorridos? '))
            break
        except:
            print('Erro: Valor digitado inválido, digite apenas números e pontos para casas decimais')
    print('-' * 40)        
    aluguel(dias, km)
    print('-' * 40)
    stop = ''
    while stop != 'N' and stop != 'S':
        stop = input('Deseja saber outro valor de aluguel? [S/N] ').strip().upper()
    if stop == 'N':
        break
print('=' * 40)
print('{:^40}'.format('Programa Finalizado!'))
print('=' * 40)