def leiadinheiro(msg):
    valor = 0
    while True:
        n = input(msg).strip().replace(',', '.')
        if n.isalpha() == True or n == '':
            print('Erro! Valor inválido: ')
        else:
            valor = float(n)
            break
    return valor
    