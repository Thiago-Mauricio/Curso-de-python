'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
 Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''

números = 'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty'
n = int(input('Digite um número entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('O número precisá estar entre 0 e 20: '))
print(f'{n} em inglés se escreve: {números[n]}')