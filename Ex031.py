n = float(input('Qual a distância em KM da sua viagem? '))
if n > 200:
    print(f'O valor da passagem ficará R${n*0.45:.2f}.')
else:
    print(f'O valor da passagem ficará R${n*0.50:.2f}.')
print('Obrigado por viajar conosco !!!')

#método do professor:
d = float(input('Qual a distância em KM da sua viagem? '))
if d <=200:
    v = d*0.50
else:
    v = d*0.45
print(f"O valor da sua passagem será de R${v:.2f}")