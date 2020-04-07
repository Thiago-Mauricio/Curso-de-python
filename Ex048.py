soma = 0
cont = 0
for c in range(0,501, 3):
    if c % 2 == 1:
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')