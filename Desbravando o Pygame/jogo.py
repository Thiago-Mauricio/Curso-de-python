def célula_check(seção):
    """
    Executa as regras do jogo da vida em um recorte 3x3 para saber o estado da cédula central
    """
    #contador de vizinhos
    vizinhos = 0
    #referencia para o centro do recorte
    centro = seção[1][1]

    #somando todos os membros do grupo
    for linha in seção:
        for célula in linha:
            vizinhos += célula
    
    #removendo o valor da célula central para somente a soma dos vizinhos
    vizinhos -= centro

    #aplicando regras do game o life
    #note que a regra dois não precisa ser ativamente aplicada, pois ela não altera o estado da célula avaliada

    if vizinhos <= 1:
        #menos de dois vizinhos a célula central morre por baixa população
        centro = 0
    elif vizinhos == 3:
        #exatamente três a célula nasce por reprodução
        centro = 1
    elif vizinhos >= 4:
        #mais que três a célula morre de super população
        centro = 0

    #retorna o valor da célula central
    return centro

def obter_seção(matriz, linha, passagem):
    """
    Extrai um recorte da vizinhança 3x3 em um plano dada a coordenada da cédula central
    """
    #monta um plano 3x3 somente com células mortas para fazer uma cópia da área a ser analisada
    seção = [[0 for _ in range(3)] for _ in range(3)]

    #percorre as redondezas da célula de posição linha x passagem copiando seu valor para seção
    for sec_r, r in enumerate(range(linha - 1, linha + 2)):
        for sec_c, c in enumerate(range(passagem - 1, passagem + 2)):
            seção[sec_r][sec_c] = matriz[r % 50][c % 50]

    #devolve o recorte 3x3 do plano
    return seção

def jogo_da_vida(seed):
    """
    Recebe uma seed de um plano 50x50 executa o game of life e devolve a geração seguinte
    """
    #cria um plano vazio para armazenar a nova geração pois não podemos
    #operar diretamente na geração corrente para não gerar efeito colateral
    nova_ger = [[0 for _ in range(50)] for _ in range(50)]

    # percorre o plano tirando recortes 3x3 da vizinhanças da célula central e os avaliando para descobrir a geração seguinte de cada cédula
    for r, linha in enumerate(seed):
        for c, passagem in enumerate(linha):
            nova_ger[r][c] = célula_check(obter_seção(seed, r, c))
    return nova_ger

