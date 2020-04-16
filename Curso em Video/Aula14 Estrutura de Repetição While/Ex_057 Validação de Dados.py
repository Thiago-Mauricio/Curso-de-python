sexo = input('Digite o seu sexo [M/F]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite apenas M ou F, tente denovo: ').strip().upper()
print('FIM')