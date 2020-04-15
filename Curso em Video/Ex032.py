from datetime import date
Ano = int(input('Qual ano quer analisar ? Coloque 0 se quiser analisar o ano atual: '))
if Ano == 0:
#comando para encontrar o ano do sistema da máquina:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print(f'{Ano} É bissexto.')
#else forma uma condição contrária ao ultimo comando de if.
else:
    print(f'{Ano} Não é bissexto.')

