from time import sleep
c = 0
print('DIGITE A BAIXO DOIS NÚMEROS PARA REALIZAR OPERAÇÕS MATEMÁTICAS:')
while c != 9:
    if c == 8:
        c = 0
    n1 = float(input('PRIMEIRO NÚMERO: '))
    n2 = float(input('SEGUNDO NÚMERO: '))
    while c != 9 and c !=8:
        print('Qual operação você deseja realizar com esses valores ? ')
        print('=' * 100)
        print(('''        [1] para somar;               [2] para multiplicar;  
        [3] para subtrair;            [4] para dividir;
        [5] para potência;            [6] para raiz quadrada;  
        [7] para saber o maior;       [8] para escolher novos números; 
        [9] para sair do programa:''').upper())
        print('=' * 100)
        c = int(input('Digite sua opção: '))
        print('=' * 100)
        if c == 1:
            print(f' {n1} + {n2} = {n1 + n2:}.')
            print('=' * 100)
            sleep(2)
        elif c == 2:
            print(f' {n1} X {n2} = {n1 * n2:}.')
            print('=' * 100)
            sleep(2)
        elif c == 3:
            print(f' {n1} - {n2} = {n1 - n2:} ')
            print('=' * 100)
            sleep(2)
        elif c == 4:
            print(f' {n1} / {n2} = {n1 / n2}')
            print('=' * 100)
            sleep(2)
        elif c == 5:
            print(f' {n1} elevado á {n2} = {n1 ** n2:.2f}')
            print('=' * 100)
            sleep(2)
        elif c == 6:
            print(f'A raiz quadrada de {n1} é {n1 ** (1/2):.2f} e a raiz quadrada de {n2} é {n2 ** (1/2):.2f}')
            print('=' * 100)
            sleep(2)
        elif c == 7:
            if n1 > n2:
                print(f'{n1} é maior que {n2}.')
                print('=' * 100)
                sleep(2)
            elif n1 == n2:
                print(f'{n1} e {n2} são iguais.')
                print('=' * 100)
                sleep(2)
            else:
                print(f'{n2} é maior que {n1}.')
                print('=' * 100)
                sleep(2)
        elif c == 0 or c > 10:
            print('Você não digitou nenhuma opção válida:')
            print('=' * 100)
            sleep(2)
print('FIM')