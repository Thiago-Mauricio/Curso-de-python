h = m = i = p = 0
print('=' *20)
print ('CADASTRO DE PESSOAS')
print('=' *20)
while True:
    idade = int(input('Idade: '))
    sexo = input('sexo: [M/F] ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo inválido: digite [M] ou [F]:').strip().upper()
    p += 1
    stop = input('Deseja cadastrar mais pessoas ? [S/N] ').strip().upper()
    while stop != 'S' and stop != 'N':
        stop = input('Comando iválido: digite [S] para ontinuar e [N] para parar: ').strip().upper()
    print('-' *20)
    if idade >= 18:
        i += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    if stop == 'N':
        break
print(f'Você cadastrou {p} pessoas, destas {i} têm mais de 18 anos; {h} são homens e {m} mulheres têm menos de 20 anos!')
print('=' *20)
print('CADRASTRO FINALIZADO !!!')
print('=' *20)