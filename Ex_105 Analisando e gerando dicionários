'''Faça um programa que tenha a função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações

-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação(opcional)'''

def notas(* num, sit=False):
    """Função para avaliar várias notas de alunos:
    :paran n: recebe uma ou mais notas
    :paran sit: valor opcional, indica situação das notas de acordo com a média
    :return: retorna um dicionário com (quantidade de notas, maior nota, menor nota, média das notas e situação(opcional))
    """
    
    alunos = {'Total':len(num), 'Maior':max(num), 'Menor': min(num), 'Média':sum(num) / len(num)}
    if sit == True:
        if alunos['Média'] < 5:
            sit = 'Ruim'
        elif 5 < alunos['Média'] < 7:
            sit = 'Razoável'
        elif 7 < alunos['Média'] < 9:
            sit = 'Boa'
        elif 9 < alunos['Média'] <= 10:
            sit = 'Excelente'
        else:
            sit = 'Média inválida'
        alunos['Situação'] = sit
    return alunos

print(notas(3, 4, 5, 7, 10,sit=True))

print(notas(7, 10, 7, 9, 8, 10, sit=True))