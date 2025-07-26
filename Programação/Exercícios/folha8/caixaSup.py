#apoia uma caixa de supermercado
##import p2c
def criar_caixa():
    """Cria um dicionario com as notas e moedas numa caixa de supermercado

    Requires: os valores introduzidos sejam inteiros
    Ensures: um dicionario com as chaves do tipo string que
             representam o tipo de moeda/nota, p.ex. notas_de_20 para as
             notas de 20, e por aí em diante, e os valores como um tuplo do tipo
             (int, float), onde int eh a quantidade de notas/moedas desse tipo
             e o float eh os euros que vale uma desse tipo
    """
    caixa = {}
    tipos_d = [('notas_de_20', 20), ('notas_de_10', 10), ('notas_de_5', 5),\
               ('moedas_de_2', 2), ('moedas_de_1', 1), ('moedas_de_50', 0.5),\
               ('moedas_de_20', 0.2), ('moedas_de_10', 0.10), ('moedas_de_05',\
                                                               0.05),\
               ('moedas_de_02', 0.02), ('moedas_de_01', 0.01)]
    for tipo in tipos_d:
        qt = int(input("Quantas " + tipo[0] + " tem na caixa? "))
        caixa[tipo[0]] = (qt, tipo[1])
    return caixa

def qt_m_caixa(caixa, tipo):
    """Da o dinheiro em caixa do tipo_m

    Requires: caixa ser um dicionario com as chaves do tipo string que
             representam o tipo de moeda/nota, p.ex. notas_de_20 para as
             notas de 20, e por aí em diante, e os valores como um tuplo do tipo
             (int, float), onde int eh a quantidade de notas/moedas desse tipo
             e o float eh os euros que vale uma desse tipo, e tipo seja uma
             string que seja uma das chaves de caixa
    Ensures: um inteiro que representa o dinheiro em caixa em notas/moedas do
             tipo especificado
    """
    r = int(caixa[tipo][0] * caixa[tipo][1])
    return r

def d_total(caixa):
    """Calcula a totalidade do dinheiro em caixa

    Requires: caixa ser um dicionario com as chaves do tipo string que
             representam o tipo de moeda/nota, p.ex. notas_de_20 para as
             notas de 20, e por aí em diante, e os valores como um tuplo do tipo
             (int, float), onde int eh a quantidade de notas/moedas desse tipo
             e o float eh os euros que vale uma desse tipo
    Ensures: um inteiro que representa o dinheiro total que ha na caixa
    """
    d_total = 0
    for i in caixa:
        d_total += caixa[i][0] * caixa[i][1]
        
    return ("%.2f"%d_total)

def trocos(custo_aquisicao, qt_entregue, caixa):
    """Calcula o troco que tem de ser entregue

    Requires: custo_aquisicao e qt_entregue sejam float ou inteiros, e que caixa
             seja um dicionario com as chaves do tipo string que
             representam o tipo de moeda/nota, p.ex. notas_de_20 para as
             notas de 20, e por aí em diante, e os valores como um tuplo do tipo
             (int, float), onde int eh a quantidade de notas/moedas desse tipo
             e o float eh os euros que vale uma desse tipo
    Ensures: um dicionario que representa o menor conjunto de notas e moedas a
             entregar de troco tendo em atencao a variedade de dinheiro em
             caixa, sendo que as chaves sao uma string que caracteriza o tipo de
             nota/moeda, p.ex. notas_de_vinte para as notas de 20, e por aí em
             diante, e os valores sao inteiros que representam a quantidade
             daquele tipo de notas/moedas que deve ser entregue para troco.
             Se nao houver na caixa suficiente para pagar, a caixa da o seu maximo
    """
    troco = qt_entregue - custo_aquisicao  #float com o troco total a ser dado
    troco_m = {}
    for i in caixa:
        i_caixa = caixa[i][0] #qt de moedas/notas que valem(cada uma) caixa[i][1]
        qt_m_i = 0
        while qt_m_i < i_caixa-1 and troco//caixa[i][1] > 0:
            troco -= caixa[i][1]
            qt_m_i += 1
            caixa[i] = (caixa[i][0]-1, caixa[i][1])
        troco_m[i] =  qt_m_i
        
    if troco != 0:
        for e in caixa:
            e_caixa = caixa[e][0] #qt de moedas/notas que valem(cada uma) caixa[i][1]
            qt_m_e = 0
            while qt_m_e < e_caixa and troco//caixa[e][1] > 0:
                troco -= caixa[e][1]
                qt_m_e += 1
                caixa[e] = (caixa[e][0]-1, caixa[e][1])
            troco_m[e] +=  qt_m_e
    return troco_m
print("Crie uma caixa de supermercado:")
caixa_m = criar_caixa()
r = input("Quer saber o total na caixa(S ou N)? ")
if r == 'S':
    print("O valor total na caixa é", d_total(caixa_m))
re = input("Quer saber que trocos teria de dar para uma certa compra(S ou N)? ")
while re == 'S':    
    if re == 'S':
        custo_m = float(input("Qual o custo da compra? "))
        qt_entregue_m = float(input("Quanto foi entregue para pagar a compra?\
"))
        dict_troco = trocos(custo_m, qt_entregue_m, caixa_m)
        print("O troco que terá de dar é: ")
        for i in dict_troco:
            if dict_troco[i] != 0:
                print(dict_troco[i], i)
    re = input("Quer saber que trocos teria de dar para outra certa compra(S \
ou N)? ")
    
