n = int(input(''))
for i in range(1, n + 1):
    if i != n + 1:
        texto_concatenado = ' '.join(str(i) for i in range(1, n + 1))  # tem um espaço ali entre as aspas!
        print(texto_concatenado, end=' ')
    else:
        texto_concatenado = ' '.join(str(i) for i in range(1, n + 1))  # tem um espaço ali entre as aspas!
        print(texto_concatenado)

# Exemplo 2
n = int(input(''))
sep = ''
for i in range(1, n + 1):
    print(sep, end='')
    print(i, end='')
    sep = ' '