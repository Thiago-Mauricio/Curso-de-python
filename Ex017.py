#método sem importar math
Co = float(input('Comprimento do cateto oposto: '))
Ca = float(input('Comprimento do cateto adj: '))
H = (Co**2+Ca**2)**(1/2)
print(f'A hipotenusa vai medir {H:.2f}.')

#com importação de math
from math import hypot

O = float(input('Comprimento do cateto oposto: '))
A = float(input('Comprimento do cateto adjacente: '))
print(f' A hipotenusa é igual á {hypot(O, A):.2f}.')
