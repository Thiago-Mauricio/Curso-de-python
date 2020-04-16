def menssagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

menssagem('Sistema de alunos')

def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)

def contador(*núm):
    print(núm)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma(* valores1):
    s = 0
    for num in valores1:
        s += num
    print(f'Somando os valores {valores1} temos {s}')

soma(2, 9, 4)