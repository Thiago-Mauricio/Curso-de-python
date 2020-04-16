def moeda(n):
    return f'R$ {n:.2f}'

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return moeda(f)

def metade(n):
    return moeda(n / 2)

def dobro(n):
    return moeda(n * 2)

def aumentar(n, p=0):
    return moeda(n + n * (p / 100))
    
def diminuir(n, p=0):
    return moeda(n - n * (p / 100))

def resumo(p, aumenta, diminui):
    print('-' * 40)
    print('{:^40}'. format('RESUMO DO VALOR'))
    print('-' * 40)
    print(f'Preço analisado:     {moeda(p)}')
    print(f'Dobro do preço :     {dobro(p)}')
    print(f'Metade do preço:     {metade(p)}')
    print(f'{aumenta}% de aumento:      {aumentar(p, aumenta)}')
    print(f'{diminui}% de redução:      {diminuir(p, diminui)}')
    print('-' * 40)