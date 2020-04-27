#map aplica um função a todos os elementos de uma lista
def fahrenheit(T):
    return (9/5) * T + 32

temp = [9, 22, 40, 90, 120]

for t in temp:
    print(fahrenheit(t))

list(map(fahrenheit, temp))

print(list(map(lambda t: (9/5) * t + 32, temp)))


#filter() aplica um função em uma lista para filtras elementos
lst = [1, 4, 5, 12, 19, 21, 22, 33]

pares = list(filter(lambda x: x % 2 == 0, lst))

print(pares)

#zip() junta elementos de listas em tuplas

x = [1, 2, 3, 7, 1, 9, 10]
y = [4, 5, 6, 1, 4, 2, 1]

print(list(zip(x, y)))

for i in zip(x, y):
    print(max(i))

#em listas de tamanhos diferentes o zip() retorna os resultados somente até o fim da menor lista
a = [1, 2, 3, 54]
b = [1, 2]
print(list(zip(a, b)))