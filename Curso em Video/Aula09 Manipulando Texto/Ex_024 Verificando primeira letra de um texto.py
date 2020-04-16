cidade = str(input('Qual o nome da sua cidade? ')).strip()
if (cidade[:6].upper()) == 'SANTO ':
    print('Sua cidade começa com a palavra Santo')
else:
    print('Sua cidade não começa com a palavra Santo.')
print('===FIM===')

#metodo profressor:
city = input('Qual o nome da sua cidade? ').strip()
print(city)
print(city[:5].upper() == 'SANTO')