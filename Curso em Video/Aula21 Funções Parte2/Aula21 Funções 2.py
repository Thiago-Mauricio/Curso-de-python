#interactive help:
help(print)
print(input.__doc__)

#doc strings:
def contador(i, f, p):
    """
    :param i: é o inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    for c in range(i, f + 1, p):
        print(c)

help(contador)

#Função com arâmetros opcionais:
def somar(a=0, b=0 ,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(1, 3)

#Escopo de variáveis:
def somar1(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar1(1, 4)
r2 = somar1(4, 6)
r3 = somar1(2, 4, 2)

print(f'Os resultados foram {r1}, {r2} e {r3}')