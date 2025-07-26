# coding: utf8

u"""Disponibiliza funções para analisar dados de temperatura.

Funções:
-- data_fraccionaria
-- ler_ficheiro
-- medias_anuais_todos_paises
-- medias_anuais_alguns_paises
-- medias_anuais
-- medias_mensais_todos_paises
-- medias_mensais_alguns_paises
-- medias_mensais
-- medias_mensais_mes_especifico_alguns_paises
-- escrever_ficheiro_data_fraccionaria
-- temperatura
-- media_das_temperaturas_mensais
-- max_das_temperaturas_mensais
-- mostra_grafico
"""
import pylab

### função de conversão do formato de data

def data_fraccionaria(ano, mes):
    u"""Converte dois inteiros representando ano e mês, numa data fraccionária.
    
    Para obter uma data fraccionária em geral: a data de uma medição é expressa
    como um ano mais a fracção decimal de um ano correspondendo ao ponto
    intermédio do período de tempo que está a ser representado.
    Exemplos apenas com ano e mês (os que são relevantes para ESTA função):
      Janeiro de 2005
        -> 2005 + (1 - 0.5) / 12 = 2005.0416666666667
      Junho de 2008
        -> 2008 + (6 - 0.5) / 12 = 2008.4583333333333
    Exemplos com ano, mês e dia (não é o caso DESTA função):
      25 de Janeiro de 2005
        -> é o dia 25 de um ano comum
        -> 2005 + (25 - 0.5) / 365 = 2005.0671232876712
      3 de Junho de 2008
        -> é o dia 155 de um ano bissexto
        -> 2008 + (155 - 0.5) / 366 = 2008.422131147541
    Requires: ano e mes são int, com 1 <= mes <= 12
    Ensures: um float que é a data fraccionária.
    """
    datafracionaria = ano + (mes-0.5) / 12;
    datafracionaria = "{:.3f}".format(datafracionaria)
    return datafracionaria


### leitura dos dados a partir de um ficheiro

def ler_ficheiro(nome_ficheiro):
    u"""Lê os dados de temperatura de um ficheiro.
    
    A 1ª linha do ficheiro (o cabeçalho) é descartada.
    Cada uma das restantes linhas é lida e dá origem a um dado de temperatura
    que é acrescentado a uma lista de dados.
    Requires: nome_ficheiro é uma string que representa o caminho para um
    ficheiro de texto; as linhas deste ficheiro, a partir da 2ª linha, têm
    de estar no formato
      país,ano,mês,temperatura
    ou seja, são 4 strings separadas por vírgulas;
    as strings devem poder ser convertidas para string, int, int e float,
    respectivamente; não podem surgir vírgulas nos nomes dos países.
    Ensures: uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura).
    """
    fich = open(nome_ficheiro)
    dados = []
    cabecalho = fich.readline()
    # print cabecalho                    # este print é usado em testes
    for linha in fich:
        dado = linha.strip().split(",")  # tudo ainda em formato lista de texto
        pais = dado[0]
        ano = int(dado[1])
        mes = int(dado[2])
        temperatura = float(dado[3]) 
        dados.append((pais, ano, mes, temperatura))
    fich.close()
    return dados


### médias anuais

def medias_anuais_todos_paises(dados, anos):
    u"""Cria uma lista com as médias anuais de temperatura para todos os países.
    
    A partir de uma lista dados que contém os valores mensais de temperatura
    em cada país, a função condensa os dados usando uma dupla média:
    sobre todos os países existentes nos dados, e sobre os 12 meses de cada ano.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos.
    Ensures: uma lista de float que são as médias anuais de temperatura para
    todos os países; esta lista de temperaturas refere-se à lista de anos que
    é passada como argumento; portanto, a lista de temperaturas tem o mesmo
    comprimento que a lista anos.

    """
    # versão que não usa dicionários
    temperaturas = [0] * len(anos) # acumula as temperaturas medidas em cada ano
    contadores = [0] * len(anos)   # nr. de registos de temperatura em cada ano
    for dado in dados:
        ano = dado[1]
        temperatura = dado[3]
        indice = ano - anos[0]
        temperaturas[indice] += temperatura
        contadores[indice] += 1
    for i in range(len(anos)):
        temperaturas[i] /= contadores[i]
    return temperaturas


def medias_anuais_alguns_paises(dados, anos, paises):
    u"""Cria uma lista com as médias anuais de temperatura para alguns países.
    
    Esta função comporta-se como medias_anuais_todos_paises(), excepto que
    só considera alguns dos países para as médias anuais.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    paises é uma lista não vazia de strings, em que pelo menos uma delas
    corresponde a um país que ocorre nos dados, tendo medições de temperatura
    em todos os anos.    
    Ensures: uma lista de float que são as médias anuais de temperatura para
    os países cujos nomes estão na lista passada como 3º argumento;
    esta lista de temperaturas refere-se à lista de anos que é passada como
    argumento; portanto, a lista de temperaturas tem o mesmo comprimento que
    a lista anos.
    """
    #reaproveitando o codigo acima
    temperaturas = [0] * len(anos) 
    contadores = [0] * len(anos)
    for dado in dados:
        for pais in paises:
            if pais == dado[0]:
                ano = dado[1]
                temperatura = dado[3]
                indice = ano - anos[0]
                temperaturas[indice] += temperatura
                contadores[indice] += 1
    for i in range(len(anos)):
        temperaturas[i] /= contadores[i]
    return temperaturas


def medias_anuais(dados, anos, paises = "todos"):
    u"""Lista com as médias anuais de temperatura para todos ou alguns países.
    
    Se paises == "todos", comporta-se como medias_anuais_todos_paises().
    Caso contrário, tem de ser passada uma lista de países no 3º argumento,
    e a função comporta-se como medias_anuais_alguns_paises(), usando os
    países da referida lista.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    paises é, opcionalmente
    -- a string "todos", ou
    -- uma lista não vazia de strings, em que pelo menos uma delas
    é o nome de um país que ocorre nos dados, tendo medições de temperatura
    em todos os anos.    
    Ensures: uma lista de float que são as médias anuais de temperatura para
    todos os países, ou são as médias anuais de temperatura para
    os países cujos nomes estão na lista passada como 3º argumento;
    a lista de temperaturas devolvida refere-se à lista de anos que
    é passada como argumento; portanto, a lista de temperaturas tem o mesmo
    comprimento que a lista anos.
    """
    temperaturas = [0] * len(anos)
    if paises == "todos":
        temperaturas = medias_anuais_todos_paises(dados, anos)
    else:
        temperaturas = medias_anuais_alguns_paises(dados, anos, paises)
    return temperaturas    


### médias mensais

def medias_mensais_todos_paises(dados, anos):
    u"""Lista de pares (mês,temperatura) com média sobre todos os países.
    
    A partir de uma lista dados que contém os valores mensais de
    temperatura em cada país, a função condensa os dados usando uma média sobre
    todos os países existentes nos dados, mas não sobre os 12 meses de cada ano.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos.
    Ensures: uma lista de pares (float,float) onde o 1º elemento de cada par é
    uma combinação ano,mês em formato fraccionário, e o 2º elemento é a
    temperatura média nesse mês para todos os países (i.e., a média, sobre os
    países, da temperatura medida nesse mês); a lista devolvida tem comprimento
    aproximadamente igual a 12 * len(anos).
    """
    temperaturas_vs_meses = []
    # optamos por listas auxiliares unidimensionais para representar todos
    # os meses no período considerado;
    # não usamos matrizes, o que seria uma opção diferente;
    # acumulando as temperaturas medidas em cada mês:
    temperaturas = [0] * len(anos) * 12
    # contando o número de registos de temperatura em cada mês:
    contadores = [0] * len(anos) * 12
    for dado in dados:
        ano = dado[1]
        mes = dado[2]
        temperatura = dado[3]
        indice = 12 * (ano - anos[0]) + mes - 1
        temperaturas[indice] += temperatura
        contadores[indice] += 1
    for i in range(len(anos) * 12):
        ano = anos[0] + i // 12
        mes = i % 12 + 1
        if contadores[i] != 0:
            temperaturas[i] /= contadores[i]
            temperaturas_vs_meses.append((data_fraccionaria(ano, mes),
                                          temperaturas[i]))
    return temperaturas_vs_meses


def medias_mensais_alguns_paises(dados, anos, paises):
    u"""Lista de pares (mês,temperatura) com média sobre alguns países.

    Esta função comporta-se como medias_mensais_todos_paises(), excepto que
    só considera alguns dos países para as médias mensais.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    paises é uma lista não vazia de strings, em que pelo menos uma delas
    corresponde a um país que ocorre nos dados, tendo medições de temperatura
    em todos os anos.  
    Ensures: uma lista de pares (float,float) onde o 1º elemento de cada par é
    uma combinação ano,mês em formato fraccionário, e o 2º elemento é a
    temperatura média nesse mês para os países cujos nomes estão na lista
    passada como 3º argumento (i.e., a média, sobre esses países, da
    temperatura medida nesse mês); a lista devolvida tem comprimento
    aproximadamente igual a 12 * len(anos).
    """
    #reaproveitando o codigo acima
    temperaturas_vs_meses = []
    temperaturas = [0] * len(anos) * 12
    contadores = [0] * len(anos) * 12
    for dado in dados:
        for pais in paises:
            if pais == dado[0]:
                ano = dado[1]
                mes = dado[2]
                temperatura = dado[3]
                indice = 12 * (ano - anos[0]) + mes - 1
                temperaturas[indice] += temperatura
                contadores[indice] += 1
    for i in range(len(anos) * 12):
        ano = anos[0] + i // 12
        mes = i % 12 + 1
        if contadores[i] != 0:
            temperaturas[i] /= contadores[i]
            temperaturas_vs_meses.append((data_fraccionaria(ano, mes),
                                          temperaturas[i]))
    return temperaturas_vs_meses

def medias_mensais(dados, anos, paises = "todos"):
    u"""Lista de pares (mês,temperatura) com média sobre todos ou alguns países.
  
    Se paises == "todos", comporta-se como medias_mensais_todos_paises().
    Caso contrário, tem de ser passada uma lista de países no 3º argumento,
    e a função comporta-se como medias_mensais_alguns_paises(), usando os
    países da referida lista.    
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    paises é, opcionalmente
    -- a string "todos", ou
    -- uma lista não vazia de strings, em que pelo menos uma delas
    corresponde a um país que ocorre nos dados, tendo medições de temperatura
    em todos os anos.
    Ensures: uma lista de pares (float,float) onde o 1º elemento de cada par é
    uma combinação ano,mês em formato fraccionário, e o 2º elemento é a
    temperatura média nesse mês para todos os países, ou para os países cujos
    nomes estão na lista passada como 3º argumento (i.e., a média, sobre esses
    países, da temperatura medida nesse mês); a lista devolvida tem comprimento
    aproximadamente igual a 12 * len(anos).
    """
    temperaturas_vs_meses = []
    if paises == "todos" :
       temperaturas_vs_meses = medias_mensais_todos_paises(dados, anos)
    else:
       temperaturas_vs_meses = medias_mensais_alguns_paises(dados,anos,paises)
    return temperaturas_vs_meses
        

### médias mensais, mês específico

def medias_mensais_mes_especifico_alguns_paises(dados, anos, paises, mes):
    u"""Lista com a temp. num certo mês ao longo dos anos, para certos países.
    
    A partir de uma lista dados que contém os valores médios mensais de
    temperatura em cada país, a função selecciona um mês e condensa os dados
    usando uma média sobre os países que são indicados no 3º argumento.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    paises é uma lista de strings representando nomes de países;
    mes é um int representando o mês pretendido, 1 <= mes <= 12
    Ensures: uma lista de float que são as médias, avaliadas sobre a lista
    de países passada como 3º argumento, das temperaturas no mês indicado,
    ao longo dos anos;
    caso não haja medições de temperatura num certo mês em nenhum dos países,
    o valor desse mês é colocado a -100.0;
    a lista de temperaturas devolvida tem o mesmo comprimento que a lista anos.    
    """
    temperatura=[0]* len(anos)
    temperatura_media=[0] * len(anos)
    
    npais=len(paises)
    ano_inicial=anos[0]
    i=0
    for pais in paises: 
        for dado in dados:     
            if dado[0] == pais:
                if dado[2] == mes:
                    temperatura[dado[1]-ano_inicial] = temperatura[dado[1]-ano_inicial]+dado[3]
    for ano in temperatura:
        temperatura_media[i]=ano/npais
        i=i+1
   
    return temperatura_media
                


### criação de ficheiro de texto com datas no formato fraccionário

def escrever_ficheiro_data_fraccionaria(dados, nome_ficheiro):
    u"""Escreve os dados, com as datas em formato fraccionário, num ficheiro.
    
    Coloca o cabeçalho "Country,Date,Temperature" como 1ª linha do ficheiro.
    Cada uma das restantes linhas corresponde à conversão, para texto, de um
    dado da lista dados passada como 1º argumento.
    A data é convertida para formato fraccionário, com arredondamento à
    terceira casa decimal; portanto, passa a ser representada por um float,
    e não por dois int.    
    As 3 strings representando as componentes dos dados são separadas por
    vírgulas.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    nome_ficheiro é uma string que representa o caminho para um ficheiro de
    texto a criar.
    Ensures: é criado um ficheiro cuja 1ª linha é "Country,Date,Temperature"
    e em que cada uma das restantes linhas contém 3 strings separadas por
    vírgulas, representando, respectivamente, país, data em formato
    fraccionário e temperatura. A data apresenta 3 casas decimais, resultantes
    de arredondamento (e não simples truncatura) à terceira casa decimal.
    """
    f = open(nome_ficheiro, 'w')
    f.writelines("Country,Date,Temperature\n")
    for dado in dados:
        f.writelines(dado[0] + "," + str(data_fraccionaria(dado[1],dado[2])) +
                     "," + str(dado[3]) + "\n")


### obter a temperatura de um ano e mês específicos, para um pais específico

def temperatura(dados, ano, mes, pais):
    u"""Temperatura de um ano e mês específicos, para um pais específico

    Procura a combinação de ano, mês e país passada nos argumentos do 2º ao 4º,
    e devolve a respectiva temperatura caso encontre essa combinação.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    ano e mes são ints correspondentes ao ano e mês a pesquisar, resp.;
    1 <= mes <= 12
    pais é uma string com o nome do país a pesquisar.
    Ensures: um float correspondente à temperatura associada a ano, mes, pais;
    caso não seja encontrada a combinação ano, mes, pais nos dados, é devolvida
    a temperatura -100.0.
    """
    temperatura = -100.0
    for dado in dados:
        if dado[0] == pais:
            if dado[1] == ano:
                if dado[2] == mes:
                    temperatura = dado[3]
    return temperatura


### obter a média das temperaturas num mês específico,
### para todos os anos, para um pais específico

def media_das_temperaturas_mensais(dados, anos, mes, pais):
    u"""Média das temps. num mês específico, todos os anos, pais específico.

    Devolve a média das temperaturas medidas sempre no mesmo mês, ao longo
    de todos os anos, para um certo país.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    mes é um int representando o mês pretendido, 1 <= mes <= 12
    pais é uma string com o nome do país a processar.
    Ensures: um float correspondente à média das temperaturas ao longo dos anos,
    sempre medidas no mês mes, para o país pais.
    """
    temperatura=0
    contagem=len(anos)
    for dado in dados:
        if dado[0] == pais:
            if dado[2] == mes:
                temperatura = temperatura+dado[3]
    temperatura_media = temperatura/contagem
    return temperatura_media
                


### obter o máximo das temperaturas num mês específico,
### para todos os anos, para um pais específico

def max_das_temperaturas_mensais(dados, anos, mes, pais):
    u"""Máximo das temps. num mês específico, todos os anos, pais específico.

    Devolve o máximo das temperaturas medidas sempre no mesmo mês, ao longo
    de todos os anos, para um certo país.
    Requires: dados é uma lista de quádruplos do tipo (string, int, int, float)
    em que cada quádruplo representa (país, ano, mês, temperatura);
    anos é uma lista de int consecutivos que representa os anos em análise;
    cada elemento da lista anos é um ano que ocorre nos dados, e cada ano que
    ocorre nos dados tem de constar na lista anos;
    mes é um int representando o mês pretendido, 1 <= mes <= 12
    pais é uma string com o nome do país a processar.
    Ensures: um float correspondente ao máximo das temperaturas ao longo dos
    anos, sempre medidas no mês mes, para o país pais.
    """
    temperatura=0
    
    for dado in dados:
        if dado[0] == pais:
            if dado[2] == mes:
                if temperatura < dado[3]:
                    temperatura = dado[3]
    temperatura_maxima=temperatura
    return temperatura_maxima

### mostrar gráfico, com opção de guardar figura num ficheiro png

def mostra_grafico(titulo_grafico, legenda_eixo_xx, legenda_eixo_yy,
                   abcissas_datasets, ordenadas_datasets, legendas_datasets, 
                   cria_ficheiro = False, nome_ficheiro = "grafico_temps"):
    u"""Cria um gráfico com séries temporais, com criação opcional de ficheiro.

    Requires: titulo_grafico é uma string que serve como título do gráfico;
    legenda_eixo_xx é uma string que serve como legenda do eixo das abcissas;
    legenda_eixo_yy é uma string que serve como legenda do eixo das ordenadas;
    abcissas_datasets é uma lista de listas, em que cada lista contém números;
    ordenadas_datasets é uma lista de listas, em que cada lista contém números;
    len(abcissas_datasets) = len(ordenadas_datasets);
    legendas_datasets é uma lista de strings, em que cada uma serve de legenda
    a um conjunto de dados, pela ordem em que os dados aparecem em
    ordenadas_datasets;
    len(legendas_datasets) = len(ordenadas_datasets);
    cria_ficheiro é um bool opcional;
    nome_ficheiro é uma string para dar nome a um ficheiro de imagem;
    é inútil instanciar o parâmetro nome_ficheiro se cria_ficheiro == False.
    Ensures: abre uma janela que mostra um gráfico contendo as séries temporais
    dos conjuntos de dados em que
    -- as abcisssas de cada um dos conjuntos de dados estão numa lista que é
       um dos elementos da lista abcissas_datasets
    -- as ordenadas de cada um dos conjuntos de dados estão numa lista que é
       um dos elementos da lista ordenadas_datasets;
    o gráfico é documentado com o título e legendas como descritos acima;
    caso cria_ficheiro seja True, é criado um ficheiro de imagem com extensão
    .png e nome dado por nome_ficheiro, que guarda o gráfico.    
    """
    i=0
    
    for absissa in abcissas_datasets:
        pylab.plot(abcissas_datasets[i], ordenadas_datasets[i], label= legendas_datasets[i])
        i=i+1
        
    pylab.legend(loc='lower right', shadow=True, fontsize=10)
    pylab.ylabel(legenda_eixo_yy)
    pylab.xlabel(legenda_eixo_xx)
    pylab.title(titulo_grafico)
    if cria_ficheiro:
        pylab.savefig(nome_ficheiro + ".png",dpi= 140 )
    pylab.show()
