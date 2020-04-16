print('Vou te mostrar uma P.A. de 10 termos!')
termo = int(input('Qual o primeiro termo da P.A.? '))
razao = int(input('Qual a razão da P.A.? '))
vezes = 0
x = 10
rodada = 0
while x != 0:
    while vezes < x:
        print(termo)
        vezes += 1
        termo = termo + razao
        rodada += 1
    vezes = 0
    x = int(input(' Te mostrei 10 termos, quantos termos vc quer ver agora? '))
print('foram mostrados ao todo {} números da P.A.'.format(rodada))