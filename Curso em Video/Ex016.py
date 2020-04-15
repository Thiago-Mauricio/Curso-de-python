import math
X = float(input('Digite um valor: '))
print(f'O valor digitado foi {X} e a sua porção inteira é {math.trunc(X)}.')
print(f'O valor difitado foi {X} e a sua porção inteira é {int(X)}.')

#esta não funciona, pois em algumas situações arredondara o numero para cima.
print(f'O valor digitado foi {X} e a sua porção inteira é {X:.0f}.')