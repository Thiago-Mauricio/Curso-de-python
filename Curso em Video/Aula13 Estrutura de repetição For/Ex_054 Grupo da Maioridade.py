from datetime import datetime
#se não usar now como variavel não funciona.
now = datetime.now()
print(now)
print('Digite a seguir 7 datas de nascimento com dia mês e ano: ')
cont = 0
cont1 = 0
data = ''
data1 = ''
for i1 in range(1,3,1):
   #replace, upper e strip para deixar o input formatado e abranger varias formatações de datas diferente e split para separar a formatação em lista
    dma = input(f'Data de nascimento {i1}: ').upper().replace('JANEIRO','01').replace('FEVEREIRO', '02').replace('MARÇO','03').replace('ABRIL', '04').replace('MAIO','05').replace('JUNHO','06').replace('JULHO','07').replace('AGOSTO','08').replace('SETEMBRO', '09').replace('OUTUBRO', '10').replace('NOVEMBRO', '11').replace('DEZEMBRO', '12') .replace(',', ' ').replace('/',' ').replace('DE', ' ').replace('DO',' ').strip().split()
   #transdormar a data em numeros inteiros e seleciona o grupo correspondente as datas para calculo posterior
    d = int(dma[0])
    m = int(dma[1])
    a = int(dma[2])
    #coloca a data dada pelo usuário no mesmo modelo da data obtida do sistema
    dob = datetime(a,m,d)
    #idade vai ser a subtração da data atual pela data preenchida pelo usuario
    dif = now - dob
    idade = dif/365.25
    #o calculo fornece alem da idade informação em horas e dias, por isso passar a idade para str e dar split para obter somente o valor da idade em anos
    idade = str(idade).split()
    #retorna idade para numero inteiro e pega só o primeiro grupo que é oda idade em si, para poder fazer o if.
    idade = int(idade[0])
    if idade >= 18:
        cont += 1
        #consegue imprimir as datas que são maiores
        data += f'{d}/{m}/{a} ',
    else:
        cont1 += 1
        #consegue imprimir as datas que são menores
        data1 += f'{d}/{m}/{a} '

print(f'Das datas de nascimento apresentadas, {cont} são maiores de idade e {cont1} são menores:')
print(data)