n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}.')
print('Que média bosta!' if m<=6 else 'Você está indo bem !!!')