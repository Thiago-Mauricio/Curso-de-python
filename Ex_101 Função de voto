'''Crie um programa que tenha uma função chamada voto() que vai receber com parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÒRIO nas eleições'''

def voto(n):
    """Calcula idade e;
    Retorna se o voto é obrigatório ou não de acordo com a idade.
    """
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 18 < idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO FACULTATIVO'


ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))