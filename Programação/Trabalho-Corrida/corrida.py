""" Modulo com funcoes para processar uma corrida.

Trabalho de Programacao I realizado pelo grupo nr. <numero com 3 digitos>

Alunos:
<45706> <Goncalo Martins>
<48691> <Henrique Baltazar>
 
Contem informacao sobre todos os atletas, incluindo a sua identificacao
e o seu desempenho na prova.
Contem funcoes para importar toda a informacao a partir de ficheiros  
externos.
 
Um atleta eh caracterizado pela sua identificacao, mas tambem
pelos resultados obtidos na prova, incluindo os resultados intermedios
em cada controlo de passagem.

Uma corrida eh caracterizada por um tuplo, que contem:
  - uma lista de atletas - contem todos os atletas, mesmo os que nao terminaram;
          inclui posicoes com dorsais sem atleta atribuido;
          a posicao de indice 0 desta lista nao eh usada
  - uma matriz arrayPosContrl - contem as posicoes (ordem de passagem) de
          TODOS os atletas em TODOS os controlos;
          a coluna de indice 0 desta matriz nao eh usada (fica com o valor 0);
          esta matriz eh na verdade uma lista de listas, ou seja, cada linha
          da matriz eh uma lista, e as linhas tem tamanhos diferentes
  - uma matriz arrayTemposContrl - contem os tempos de passagem de
          TODOS os atletas em TODOS os controlos, em segundos;
          a coluna de indice 0 desta matriz nao eh usada (fica com o valor 0);
          esta matriz eh na verdade uma lista de listas, ou seja, cada linha
          da matriz eh uma lista, e as linhas tem tamanhos diferentes
"""

from atleta import setPosContrl, setTemposContrl, criaAtleta, getDorsal, getTodosControlosValidos, stringAtleta

def criaCorrida(fichAtletas, listaFichsPosContrl, listaFichsTemposContrl):
    """ Cria um tuplo, com a identificacao e com os resultados dos atletas

    Requires: fichAtletas seja uma string com o nome do ficheiro contendo
                  a identificacao dos atletas
              listaFichsPosContrl seja uma lista de nomes de ficheiros
                  contendo as posicoes dos atletas nos controlos 
              listaFichsTemposContrl seja uma lista de nomes de ficheiros
                  contendo os tempos de passagem dos atletas nos controlos
    Ensures: um tuplo contendo a identificacao de todos os atletas e as suas
             posicoes e tempos em cada controlo
    """
    
    atletas = leAtletas(fichAtletas)
    arrayPosContrl = lePosicoes(listaFichsPosContrl)
    arrayTemposContrl = leTempos(listaFichsTemposContrl)
    completaResultsAtletas(atletas, arrayPosContrl, arrayTemposContrl)

    return (atletas, arrayPosContrl, arrayTemposContrl)


def lePosicoes(listaFichsPosContrl):
    """ Le os ficheiros com as posicoes nos diferentes controlos

    Abre ficheiros cujos nomes estao na lista listaFichsPosContrl e le desses 
    ficheiros listas de dorsais, ordenadas pela posicao de cada atleta ao 
    passar em cada controlo.
    
    Exemplo: se um atleta passou um certo controlo registado na posicao 75,
    o seu dorsal aparece na linha 75 do ficheiro associado a esse controlo.
    
    Ha um ficheiro destes por cada controlo, incluindo o controlo 0 (partida).

    O conteudo de cada ficheiro eh armazenado numa linha da matriz
    arrayPosContrl.
    O valor inteiro codificado por cada string eh guardado como um int
    na matriz arrayPosContrl.
        
    Requires: listaFichsPosContrl seja uma lista de nomes de ficheiros contendo
              as posicoes dos atletas nos controlos 
    Ensures: uma matriz contendo as posicoes dos atletas em cada controlo
    """    
    matriz = []
    controlo = 0
    
    for ficheiro in listaFichsPosContrl:
        inFile = open(ficheiro, 'rU')  # U para compatibilidade com varios SOs

        matriz.append([])
        matriz[controlo].append(0)

        for line in inFile:
            matriz[controlo].append(int(line))

        controlo += 1
        inFile.close()
                
    return matriz
        
 
def leTempos(listaFichsTemposContrl):
    """ Le os ficheiros com os tempos nos diferentes controlos

    Abre ficheiros cujos nomes estao na lista listaFichsTemposContrl e le
    desses ficheiros listas de tempos de passagem, ordenadas pela posicao
    de cada atleta ao passar em cada controlo.

    Exemplo: se um atleta passou um certo controlo na posicao 75, o seu tempo 
    de passagem aparece na linha 75 do ficheiro de tempos correspondente
    a esse controlo.

    Os tempos estao no formato hh:mm:ss.

    Ha um ficheiro destes por cada controlo.

    Todos os atletas ficam com tempo 00:00:00 na partida (controlo 0).

    O conteudo de cada ficheiro eh armazenado numa linha da matriz
    arrayTemposContrl.
    Cada string no formato hh:mm:ss eh convertida no equivalente em
    segundos e esse valor eh guardado como um int na matriz
    arrayTemposContrl.
    
    Requires: listaFichsTemposContrl seja uma lista de nomes de ficheiros
              contendo os tempos dos atletas nos controlos 
    Ensures: uma matriz contendo os tempos dos atletas em cada controlo
    """
    matriz = []
    controlo = 0
    
    for ficheiro in listaFichsTemposContrl:
        inFile = open(ficheiro, 'rU')  # U para compatibilidade com varios SOs

        matriz.append([])
        matriz[controlo].append(0)

        for line in inFile:
            split_line = line.split(':')
            segundos = int(split_line[0]) * 3600
            segundos += int(split_line[1]) * 60
            segundos += int(split_line[2])
            matriz[controlo].append(segundos)

        controlo += 1
        inFile.close()
                
    return matriz


def leAtletas(fichAtletas):
    """ Le o ficheiro com a identificacao dos atletas

    Abre o ficheiro com nome fichAtletas e le desse ficheiro a identificacao
    de todos os atletas.
     
    Cada triplo de linhas do ficheiro contem os dados de 1 atleta:
    -- numero de dorsal (etiqueta numerica identificativa);
    -- nome;
    -- escalao (sigla informando faixa etaria e genero masculino/feminino).
    
    Caso nao haja um atleta atribuido a um dado dorsal, isso eh indicado
    nas duas linhas que se seguem ah do numero desse dorsal usando
    'nao atribuido' em vez de um nome de atleta, e
    'N/A' em vez de um escalao.

    Em geral, o numero de atletas eh inferior ao numero de dorsais, por haver
    dorsais nao atribuidos.  
    
    Requires: fichAtletas seja uma string contendo o nome do ficheiro com a 
              informacao dos atletas
    Ensures: uma lista contendo todos os atletas; o dorsal 0 nao eh utilizado
    """    
    atletas = []
    atletas.append([0, '', '', [], []])
    
    inFile = open(fichAtletas, 'rU')  # U para compatibilidade com varios SOs
    lines = inFile.readlines()
    inFile.close()
    
    for i in range (0, len(lines), 3):
        num = int(lines[i])
        nome = lines[i+1].rstrip('\n')
        escalao = lines[i+2].rstrip('\n')
        
        atletas.append(criaAtleta(num, nome, escalao))

    return atletas


def completaResultsAtletas(atletas, arrayPosContrl, arrayTemposContrl):
    """ Completa a informacao dos atletas com os resultados da corrida

    Apos estarem instanciadas as matrizes com as posicoes e tempos de passagem
    de todos os atletas em todos os controlos, os atributos dos atletas sao
    completados com essa informacao, individualmente para cada atleta.
    
    Requires: atletas seja uma lista de atletas
              arrayPosContrl seja uma matriz com as posicoes dos atletas
              arrayTempoContrl seja uma matriz com os tempos dos atletas
    Ensures: actualiza a lista de atletas com a informacao sobre a corrida
    """
    for a in atletas:
        setPosContrl(a, arrayPosContrl)
        setTemposContrl(a, arrayTemposContrl)


def escreveClassGeralFich(corrida, fichClassGeral):
    """ Escreve um ficheiro com os resultados dos atletas que cortaram a meta

    Abre um ficheiro com nome fichClassGeral e escreve nesse ficheiro os
    resultados finais de todos os atletas que cortaram a meta.
    
    Os resultados sao registados respeitando a ordem de chegada: a primeira
    linha do ficheiro regista os dados e desempenho do primeiro atleta a cortar
    a meta, a segunda linha regista os do segundo atleta, e assim sucessivamente
    ate ao ultimo atleta que cortou a meta.
     
    Os dados de cada atleta estao na lista de atletas.
    As posicoes na meta coincidem com as posicoes no ultimo controlo,
    as quais podem ser lidas da matriz arrayPosContrl pela ordem correcta
    (ordem crescente).
    Os tempos de chegada coincidem com os tempos no ultimo controlo.
     
    Exemplo de uma linha escrita no ficheiro; deve-se respeitar este formato:
 
      1 | dorsal 563 | 03:18:57 | IGOR TIMBALARI (VT1M)

    No formato ilustrado, as strings correspondem sucessivamente a
    -- posicao na meta;
    -- numero de dorsal;
    -- tempo na meta;
    -- nome;
    -- escalao.
    
    Requires: corrida seja um tuplo com a informacao sobre a corrida
              fichClassGeral seja uma string com o nome do ficheiro a criar
    Ensures: cria um ficheiro, de nome fichClassGeral, com a informacao dos
                nAtletasFinal que cortaram a meta
    """
    # INSERIR CODIGO AQUI
    
    cl = []    
    atletas=getAtletas(corrida)

    # O key = lambda x: permite fazer sort de uma lista com base em sub-elementos
    # de uma lista.
    atletas = sorted(atletas, key = lambda x: int(x[3][3]))

    #adiciona ah lista os que chegaram ao fim da corrida.
    for atleta in atletas:
        if getTodosControlosValidos(atleta):
            cl.append(atleta)
        else:
            continue

    #escreve novo ficheiro e escreve com o formato pretendido.
    with open(fichClassGeral, "w") as outfile:
        for atleta in cl:        
            outfile.write(stringAtleta(atleta) + "\n")


def dorsalNaPosicaoNoEscalao(corrida, escalaoPretendido, posicaoPretendida):
    """ Devolve o numero de dorsal do atleta que chegou na posicao
    posicaoPretendida considerando apenas o subconjunto de atletas do
    escalao escalaoPretendido

    Se posicaoPretendida for superior ao numero de atletas no escalao
    escalaoPretendido que terminaram a corrida, a funcao devolve 0.
    
    Requires: corrida           seja um tuplo com a informacao sobre a corrida
              escalaoPretendido seja uma string com o escalao a pesquisar
              posicaoPretendida seja um int com a posicao a pesquisar
    Ensures: um int com o dorsal do atleta que chegou na posicao pretendida
    """    
    # INSERIR CODIGO AQUI
    
    atletas_escalao = []
    atletas_pos = []
    atletas_pos.append([0, '', '', [], []])
    
    #Ciclo for: que faz append para uma lista apenas com atletas consoante o escalaoPretendido;
    for atleta in getAtletas(corrida):
        if atleta[2] == escalaoPretendido:
            atletas_escalao.append(atleta)

    #Dentro dessa lista, para cada atleta, procura a sua posicao no ultimo controlo.
    #Em vez dos dois ciclos for nested, poderia-se usar novamento a funcao lambda do
    #do escreveClassGeralFich, ou criar esta funcao e depois chama-la nas duas. 
    for posicao in getArrayPos(corrida)[3]:
        for atleta in atletas_escalao:
            if posicao == getDorsal(atleta):
                atletas_pos.append(atleta)

    #Para o caso da posicao pretendida for superior ao numero de atletas no escalao pretendido       
    if len(atletas_escalao) < posicaoPretendida:
        return 0
    else:
        return atletas_pos[posicaoPretendida][0]
                
            
def getAtletas(corrida):
    """ Devolve a lista de atletas desta corrida

    Requires: corrida seja um tuplo com a informacao da corrida
    Ensures: uma lista com os atletas da corrida
    """    
    return corrida[0]
  

def getArrayPos(corrida):
    """ Devolve a matriz com as posicoes de passagem nos controlos

    Requires: corrida seja um tuplo com a informacao da corrida
    Ensures: uma matriz com as posicoes de passagem nos controlos
    """    
    return corrida[1]


def getArrayTempos(corrida):
    """ Devolve a matriz com os tempos de passagem nos controlos

    Requires: corrida seja um tuplo com a informacao da corrida
    Ensures: uma matriz com os tempos de passagem nos controlos
    """    
    return corrida[2]


