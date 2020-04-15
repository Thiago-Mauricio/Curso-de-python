from datetime import date
nas = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nas
if idade < 18:
    print(f'Você ainda não chegou no periodo de alistamento. Faltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print(f'Você precisa se alistar neste ano !!!')
else:
    print(f'Você já passou {idade - 18} anos do período de alistamento.')