#apoia uma caixa de supermercado
##import p2c
def qt_m_caixa(d_caixa, tipo_m):
    """Da o dinheiro em caixa do tipo_m

    Requires: d_caixa(dinheiro em caixa) seja um float que represente
              o dinheiro total em caixa e tipo_m seja o tipo de
              moedas/notas que se quer saber a quantidade em caixa, sendo p.ex
              as notas de 20 representadas por n_20, ..., as moedas de 2€ por
              m_2, as de 20 centimos por m_20, as de dois centimos por m_02,
              e por ai em diante
    Ensures: um inteiro que representa a
             quantidade de notas do tipo_m que estam na caixa, sendo que ha
             o maximo possivel de notas de 20, depois de 10, a seguir de 5,
             e assim em diante(o maximo sao as notas de 20), e a posicaao 1
             eh um dicionario cujas chaves sao sendo o tipo de nota
             ou moeda, p.ex. as notas de 20 representadas por n_20, ...,
             as moedas de 2€ por m_2, as de 20 centimos por m_20, as de dois
             centimos por m_02, e por ai em diante
    """
    atualizacao_d = d_caixa
    d_caixa_m = {}
    d_caixa_m['n_20'] = int(d_caixa //20)
    atualizacao_d -= d_caixa_m['n_20']*20
    d_caixa_m['n_10'] = int(atualizacao_d //10)
    atualizacao_d -= d_caixa_m['n_10']*10
    d_caixa_m['n_5'] = int(atualizacao_d //5)
    atualizacao_d -= d_caixa_m['n_5']*5
    d_caixa_m['m_2'] = int(atualizacao_d //2)
    atualizacao_d -= d_caixa_m['m_2']*2
    d_caixa_m['m_1'] = int(atualizacao_d //1)
    atualizacao_d -= d_caixa_m['m_1']*1
    d_caixa_m['m_50'] = int(atualizacao_d //0.5)
    atualizacao_d -= d_caixa_m['m_50']*0.5
    d_caixa_m['m_20'] = int(atualizacao_d //0.2)
    atualizacao_d -= d_caixa_m['m_20']*0.2
    d_caixa_m['m_10'] = int(atualizacao_d //0.1)
    atualizacao_d -= d_caixa_m['m_10']*0.1
    d_caixa_m['m_05'] = int(atualizacao_d //0.05)
    atualizacao_d -= d_caixa_m['m_05']*0.05
    d_caixa_m['m_02'] = int(atualizacao_d //0.02)
    atualizacao_d -= d_caixa_m['m_02']*0.02
    d_caixa_m['m_01'] = int(atualizacao_d //0.01)
    
    return (int(d_caixa_m[tipo_m]), d_caixa_m)



##print("n_20", qt_m_caixa(134.77, "n_20")[0])
print("n_10", qt_m_caixa(134.77, 'n_10')[0])
##print("n_5", qt_m_caixa(134.77, 'n_5')[0])
##print("m_2", qt_m_caixa(134.77, 'm_2')[0])
##print("m_1", qt_m_caixa(134.77, 'm_1')[0])
##print("m_50", qt_m_caixa(134.77, 'm_50')[0])
##print("m_20", qt_m_caixa(134.77, 'm_20')[0])
##print("m_10", qt_m_caixa(134.77, 'm_10')[0])
##print("m_05", qt_m_caixa(134.77, 'm_05')[0])
##print("m_02", qt_m_caixa(134.77, 'm_02')[0])
##print("m_01", qt_m_caixa(134.77, 'm_01')[0])

##c_caixa(conteudo da caixa) seja um dicionario com as chaves
##sendo floats que representam o tipo de moeda/nota, p. ex.
##20(vinte euros), 0.5(50 centimos), e os valores com sendo
##a quantidade de 
