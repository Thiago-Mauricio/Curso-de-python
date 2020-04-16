peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    imc = 'Abaixo do peso'
elif imc < 25:
    imc = 'Com o peso ideal'
elif imc < 30:
    imc = 'Com sobrepeso'
elif imc < 40:
    imc = 'Com obesidade'
else:
    imc = 'Com obesidade morbida'
print(f'O seu imc é de {peso / (altura * altura):.1f} você está : {imc}.')