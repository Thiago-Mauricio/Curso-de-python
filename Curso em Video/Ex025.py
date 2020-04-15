nome = input('Digite o seu nome completo: ')
N = nome.upper()
if N.find('SILVA') == -1:
    print('Seu nome não possui a palavra Silva')
else:
    print('Seu nome possui a palavra Silva.')