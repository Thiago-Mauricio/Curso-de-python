frase = 'Curso em Video Python'

# Fatiamento:
print(frase[9])
print(frase[9:21])
print(frase[9:20:2])
print(frase[9::3])

# Análise:
print(len(frase))  # comprimento
print(frase.count('o'))  # contagem de caracteres especificos:
print(frase.count('o', 0, 13))  # contagem com fatiamento.
print(frase.find('o'))  # procura caracteres e informa onde está o primeiro resultado.
print('Curso' in frase)

# Transformação:
print(frase.replace('Python', 'Android'))  # substitui caracteres
print(frase.upper())  # transforma todas as letras em maiusculas.
print(frase.lower())  # minusculas
print(frase.capitalize())  # coloca a primeira letra da frase em maiuscula e o resto em minuscula
print(frase.title())  # coloca a primeira letra de todas as palavras em maiusculas
frase1 = '   Aprenda Python   '
print(frase1.strip())  # retira os espaços inuteis, pode ser usado 'rstrip' ou 'lstrip' para retirar espaços de um lado só .

# Divisão:
print(frase.split())  # separa cada palavra em uma nova lista
dividido = frase.split()
print(''.join(dividido))  # junta a frase
