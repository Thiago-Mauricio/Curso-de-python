s = float(input('Salário atual: '))
if s > 1250:
    print(f'O valor do reajuste será de R${s*0.10:.2f} e o salário total será de R${s*0.10+s:.2f} ')
else:
    print(f'O valor do reajuste será de R${s*0.15:.2f} e o salário total será de R${s*0.15+s:.2f}')
