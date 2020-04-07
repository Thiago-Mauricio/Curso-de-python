D = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km o carro percorreu? '))
A = (D * 60) + (Km * 0.15)
print(f'O total a pagar é de {A:.2f}R$.')
