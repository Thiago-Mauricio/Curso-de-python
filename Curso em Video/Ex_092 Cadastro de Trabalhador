'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre os(com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário rebeberá também o ano de contratação e o salário. Calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
ano = date.today().year
Registro = {}
Registro['Nome'] = input('Nome: ')
Nascimento =  int(input('Ano de Nascimento: '))
Registro['Nascimento'] = ano - Nascimento
Registro['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
if Registro['CTPS'] != 0:
    Registro['Salário'] = float(input('Salário: '))
    Registro['Contratação'] = int(input('Ano de contratação: '))
    for v, k in Registro.items():
        print(f'{v} tem o valor: {k}')
    print(f'Idade de aposentadoria é: {Registro["Contratação"] - Nascimento + 35} anos')
else:
    for v, k in Registro.items():
        print(f'{v} tem o valor: {k}')
