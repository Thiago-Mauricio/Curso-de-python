'''Cria um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobor() e metade()
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from UtilidadesCeV import moedas
from UtilidadesCeV import dados

p = dados.leiadinheiro('Digite o preço: R$')
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(f'Aumentando 10% o preço, temos {moedas.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13)}')

moedas.resumo(p, 80, 35)