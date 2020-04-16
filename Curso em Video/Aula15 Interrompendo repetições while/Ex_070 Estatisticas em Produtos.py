s = p = b = c = 0
n = ''
print('=' * 60)
print('CARRINHO DE COMPRAS:')
print('=' * 60)
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produro: R$'))
    s += preço
    c += 1
    if preço > 1000:
        p += 1
    if c == 1 or preço < b:
        b = preço
        n = nome
    stop = input('Deseja continuar ? [S/N] ').strip().upper()
    print('-' * 60)
    while stop != 'S' and stop != 'N':
        stop = input('Comando inváildo: digite [S/N]: ').strip().upper()
    if stop == 'N':
        break
print(f'O valor total dos produtos é de R$:{s:.2f}.')
print(f'{p} produto(s) custam mais de R$:1000.00.')
print(f'O produto mais barato é {n} e custa R$:{b:.2f}.')
print('=' * 60)