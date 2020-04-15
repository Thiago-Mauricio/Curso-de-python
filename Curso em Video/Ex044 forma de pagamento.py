from unidecode import unidecode
valor = float(input('Valor do produto: '))
forma = input('A forma de pagamento será dinheiro, cheque ou cartão? ').strip()
f = unidecode(forma.upper())
valorcv = valor - (valor * 0.05)
if f in 'DINHEIRO CHEQUE':
    valor = valor - (valor * 0.1)
    print(f'O valor do produto com a forma de pagamento selecionada será de R${valor:.2f}')
elif f == 'CARTAO':
    c = input('A vista, débito ou parcelado? ').strip()
    c1 = unidecode(c.upper())
    if c1 == 'A VISTA':
        valor = valorcv
        print(f'O valor do produto com a forma de pagamento selecionada será de R${valor:.2f}')
    elif c1 == 'DEBITO':
        valor = valor - (valor * 0.1)
        print(f'O valor do produto com a forma de pagamento selecionada será de R${valor:.2f}')
    elif c1 == 'PARCELADO':
        p = int(input('Quantas parcelas? '))
        if p <= 2:
            valor = valor
            print(f'O valor do produto com a forma de pagamento selecionada será de R${valor:.2f}')
        else:
            valor = valor + (valor *  0.2)
            print(f'O valor do produto com a forma de pagamento selecionada será de R${valor:.2f}')
    else:
        print('Forma de pagamento inválida, tente novamente.')
else:
    print('Forma de pagamento invalida, tente novamente.')
