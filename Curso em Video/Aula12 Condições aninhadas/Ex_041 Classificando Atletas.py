from datetime import date
nas = int(input('Ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nas
if idade <= 9:
    print(f'O atleta tem {idade} anos e pertence a categoria Mirim.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e pertence a categoria Infantil.')
elif idade <= 19 :
    print(f'O atleta tem {idade} anos e pertence a categoria Junior.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e pertence a categoria Sênior.')
else:
    print(f'O atleta tem {idade} anos e pertence a categoria Master.')