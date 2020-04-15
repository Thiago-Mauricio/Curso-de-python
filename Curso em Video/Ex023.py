num = int(input('Digite um numero de 0 á 9999: '))
num1 = str(num)
print(f'Analisando o número {num}:')
if num >=10000:
    print('Este numero é maior que 9999.')
else:
    if len(num1) == 1:
        num1 = 0,0,0,num1
    if len(num1) == 2:
        num1 = 0,0,num1[0],num1[1]
    if len(num1) == 3:
        num1 = 0,num1[0],num1[1],num1[2]
    print(f'Esse número tem {num1[0]} milhar(es)')
    print(f'Esse número tem {num1[1]} centena(s)')
    print(f'Esse número tem {num1[2]} dezena(s)')
    print(f'Esse número tem {num1[3]} unidade(s)')

print('=' *30)
#Maneira matemática
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Esse número tem {m} milhar(es)')
print(f'Esse número tem {c} centena(s)')
print(f'Esse número tem {d} dezena(s)')
print(f'Esse número tem {u} unidade(s)')

print('=' *30)
#modelo mais simples:
z1 = int(input('Digite um numero de 0 á 9999: '))
z = str(z1).zfill(4)
if z1 >=10000:
    print('Este numero é maior do que 9999')
else:
    print(f'Esse número tem {z[0]} milhar(es)')
    print(f'Esse número tem {z[1]} centena(s)')
    print(f'Esse número tem {z[2]} dezena(s)')
    print(f'Esse número tem {z[3]} unidade(s)')