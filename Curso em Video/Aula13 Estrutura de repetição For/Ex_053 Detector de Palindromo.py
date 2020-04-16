from unidecode import unidecode
f = input('Escreva uma frase : ').strip()
#retirando toda a pontuação com . replace
f1 =f.upper().replace(',', '').replace('.','').replace('!','').replace('?','').replace('-','').replace('_','')
#poderia trocar .split e . join por .replace(' ',''), mas quis deixar do jeito que idealizei primeiro
l = f1.split()
#unidecode tira a acentuação
f2 = unidecode(''.join(l))
if f2[::-1] == f2:
    print(f'{f} é uma frase pálindromo')
else:
    print(f'{f} não é uma frase pálindromo')

#método com for do professor:
inverso = ''
#acho f2[::-1] é uma forma muito mais simples e prática para inverter uma string
for letra in range(len(f2) -1, -1, -1):
    inverso +=f2[letra]
if inverso == f2:
    print('Temos um pálindromo!')
else:
    print('Não temos um pálindromo')