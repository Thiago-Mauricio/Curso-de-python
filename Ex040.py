n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Sua média foi {m:.1f}. Você foi reprovado.')
elif 7 > m >= 5:
#elif m >= 5 and m <= 6.9:
    print(f'Sua média foi {m:.1f}. Você está de recuperação.')
else:
    print(f'Sua média foi {m:.1f}. Você foi aprovado !!!')