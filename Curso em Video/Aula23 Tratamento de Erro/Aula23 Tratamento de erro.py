try:
    a = int(input('Numrador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print(f'Tivemos um erro ')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')