casa = float(input('Qual o valor da casa que deseja comprar? '))
salário = float(input('Qual o seu salário mensal? '))
meses= int(input('Em quantos meses você pretende pagar a casa? '))
parcela = (casa / meses)
if parcela > salário * 0.30:
    print('Infelizmente o seu empréstimo foi negado')
else:
    print(f'O empréstimo foi aprovado e o valor da sua parcela será de R${parcela:.2f} por mês.')