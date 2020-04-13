'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''

def fatorial(n, show=False):
    """
    para n: O numero a ser calculado.
    para show: (opcioanl) Mostra ou nao o processo de conta.
    return: O valor faltorial de um numero em n
    """
    f = 1
    cont = n
    for c in range(n, 0, -1):
        f *= c
        cont -= 1
        if show == True:
            print(c, end ='')
            print(' X ' if cont >= 1 else ' = ',end='')
    return f
    


print(fatorial(5, show=True))
help(fatorial)