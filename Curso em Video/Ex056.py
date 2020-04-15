#soma para obter a média:
soma = 0
#somátorio da idade do mais velho
mv = 0
#contador de mulheres abaixo de 20
cont = 0
velho = 'Não há homens nesse grupo'
for c in range(1,5):
    print('-' * 10, f'{c}ª PESSOA', '-' * 10)
    nome = input('Digite seu nome: ').strip()
    idade = input('Digite sua idade: ')
    while bool(idade.isnumeric()) == False :
            idade = input('Digite apenas numeros na sua idade:').strip()
    idade = int(idade)
    sexo = input('Digite seu sexo> [M/F]: ').upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo inválido, a resposta deve ser M ou F. Digite novamente seu sexo: ').upper().strip()
    soma = soma + idade
    #separando os grupos em M e F
    if sexo == 'M':
        #selecioando o homem mais velho
        if c == 1:
            mv = idade
            velho = nome
        else:
            if idade > mv:
                mv = idade
                velho = nome
    else:
        #contando a quantidade de mulheres abaixo dos 20 anos:
        if idade < 20:
            cont += 1
média = soma / 4
print(f'A média de idade do grupo é de {média}.')
print(f'O homem mais velho do grupo é {velho.capitalize()} que tem {mv} anos.')
print(f'{cont} mulher(es) possue(m) menos de 20 anos.')