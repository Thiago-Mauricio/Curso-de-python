v = float(input('Velocidade atual do carro: '))
if v > 80:
    print('Você ultrapassou o limite de velocidade de 80km/h, e por isso receberá uma multa com o valor de R$7.00 para cada Km acima do limite')
    print(f'O valor da sua multa é de R${(v-80)*7:.2f}')
else:
      print('Obrigado por respeitar o limite de velocidade !!!')