""" Modulo com funcoes para processar a info de atletas.

Trabalho de Programacao I realizado pelo grupo nr. <numero com 3 digitos>

Alunos:
<45706> <Goncalo Martins>
<48691> <Henrique Baltazar>

Contem funcoes para processar informacao sobre cada atleta,
obtida a partir de matrizes que contem informacao sobre todos os atletas
em cada um dos locais de controlo de passagem.
 
Um atleta eh caracterizado por um tuplo, que contem:
  - um int correspondente ao numero do dorsal
  - uma string com o nome do atleta
  - uma string com o escalao a que pertence o atleta
  - uma lista com as posicoes do atleta em cada controlo
  - uma lista com os tempos (em segundos) do atleta, em cada controlo
"""

import pylab
import time

def criaAtleta(numDorsal, nome, escalao):
    """ Cria um tuplo correspondendo a um atleta

    Requires: numDorsal seja um int   - o numero de dorsal do Atleta
              nome seja uma string    - o nome do Atleta
              escalao seja uma string - o escalao do Atleta
    Ensures:  um tuplo contendo a identificacao de um atleta,
              mas ainda sem resultados da prova
    """
    return (numDorsal, nome, escalao, [], [])


def getDorsal(atleta):
    """ Devolve o numero do dorsal do atleta

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  um int com o numero do dorsal do atleta
    """    
    return atleta[0]


def getNome(atleta):
    """ Devolve o nome do atleta

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  uma string com o nome do atleta
    """
    return atleta[1]

  
def getEscalao(atleta):
    """ Devolve o escalao do atleta

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  uma string com o escalao do atleta
    """
    return atleta[2]

  
def encontraPosicao(atleta, arrayPosContrl, controlo):
    """ Devolve a posicao do atleta aquando da passagem pelo controlo indicado

    A posicao eh encontrada pesquisando ao longo da linha controlo da matriz
    arrayPosContrl. 
    Se o atleta nao for encontrado no controlo, a funcao devolve 0. 
    Requires: atleta seja um tuplo contendo informacao do atleta
              arrayPosContrl seja uma matriz contendo as posicoes de passagem de 
                             todos os atletas em todos os controlos
              controlo seja um int com o numero do controlo que se pretende
                       pesquisar
    Ensures:  um int com a posicao do atleta no controlo

    NB: arrayPosContrl eh uma matriz com linhas de tamanho nao uniforme;
    na verdade, esta matriz eh uma lista de listas.
    
    Para melhor entender a estrutura da matriz arrayPosContrl, consultar:
      -- a docstring que documenta o modulo corrida (aparece no inicio do
         respectivo ficheiro)
      -- a docstring que documenta a funcao lePosicoes do modulo corrida

    Nao eh usado o elemento de indice 0 em cada uma das listas que contem as
    posicoes de passagem dos atletas nos controlos. Assim, a posicao de passagem
    do atleta no controlo coincide com o indice na lista onde a posicao desse
    atleta estah registada; portanto, nao eh (indice + 1).
    """
    # INSERIR CODIGO AQUI

    if getDorsal(atleta) in arrayPosContrl[controlo]:
        return arrayPosContrl[controlo].index(getDorsal(atleta))
    else:
        return 0


def getPosContrl(atleta):
    """ Devolve a sequencia de posicoes do atleta

    Se o atleta nao tiver passado num certo controlo, a posicao
    nesse controlo eh 0
    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  uma lista com a sequencia de posicoes do atleta
    """    
    return atleta[3]
  
  
def getTemposContrl(atleta):
    """ Devolve a sequencia de tempos de passagem do atleta

    Se o atleta nao tiver passado num certo controlo, o tempo de passagem
    nesse controlo eh 0
    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  uma lista com a sequencia de tempos de passagem do atleta
    """    
    return atleta[4]
  

def getTodosControlosValidos(atleta):
    """ Determina se este atleta passou em todos os controlos

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  um bool que eh True so se o Atleta passou em todos os controlos
    """
    # INSERIR CODIGO AQUI
    
    if 0 in getPosContrl(atleta):
        return False
    else:
        return True


def mostraSequenciaPosicoes(atleta):
    """ Mostra no output standard a sequencia de posicoes do atleta

    A posicao na partida (controlo 0) tambem eh mostrada, pois os atletas
    nao cruzam a linha de partida em simultaneo (apesar de ficarem todos
    com o tempo 00:00:00 na partida).

    A posicao num controlo pode ser 0 (zero), correspondendo ao caso em que
    o atleta nao passou nesse controlo. Nesse caso, eh impressa a posicao 0.

    Exemplo de output:

    Sequencia de posicoes do atleta com o dorsal 322:
    controlo 0: posicao 44
    controlo 1: posicao 11
    controlo 2: posicao 8
    controlo 3: posicao 8

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  imprime a sequencia de posicoes do atleta nos diferentes controlos
    """    
    print ("\nSequencia de posicoes do atleta com o dorsal", getDorsal(atleta))

    controlo = 0

    # for i in atleta[3]:
    for i in getPosContrl(atleta):
        print("controlo", controlo, ": posicao", i)
        controlo += 1


def desenhaSequenciaPosicoes(atleta):
    """ Abre uma janela com uma figura com a sequencia de posicoes do atleta

    A posicao na partida (controlo 0) tambem eh mostrada, pois os atletas
    nao cruzam a linha de partida em simultaneo (apesar de ficarem todos
    com o tempo 00:00:00 na partida).

    A posicao num controlo pode ser 0 (zero), correspondendo ao caso em que o
    atleta nao passou nesse controlo. Nesse caso, eh mostrada a posicao como 0.

    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  abre uma janela onde eh desenhado um grafico que mostra
              a sequencia de posicoes do atleta nos diferentes controlos

    Por exemplo, para o atleta 322, eh criado um grafico semelhante ao que
    pode ser visto no ficheiro posicoes-atleta_322.pdf.
    A figura deve ser configurada como estah exemplificado
    no ficheiro pdf referido.
    """
    # INSERIR CODIGO AQUI
    
    pylab.figure(1)

    numdorsal = getDorsal(atleta)
    nome = getNome(atleta)

    pylab.title ('Posicoes do atleta ' + str(numdorsal) + ' ' + nome)
    pylab.xlabel ('Controlos')
    pylab.ylabel ('Posicoes')
    pylab.plot ( [0,1,2,3], getPosContrl(atleta), '-o')
    pylab.xticks(range(4))
    pylab.figure(1).patch.set_facecolor('white')
    pylab.show()
    
    
def stringAtleta(atleta):
    """ Obtem uma representacao textual deste atleta

    A representacao pode ser usada para imprimir e.g. com print
    ou para guardar a string num ficheiro.

    O formato da string eh o seguinte:

      3 | dorsal 412 | 03:23:34 | BENEK MORAIS (VT1M)

    Respectivamente: posicao na meta (ocupando 3 espacos, alinhada ah direita),
    identificacao do dorsal, tempo na meta, nome, escalao.

    Se o atleta nao chegou a meta, a posicao e o tempo final ficam a zero. 
    Requires: atleta seja um tuplo contendo informacao do atleta
    Ensures:  uma string com a representacao textual deste atleta
    """    
    posMeta = getPosContrl(atleta)[len(getPosContrl(atleta)) - 1]
    tempoMeta = getTemposContrl(atleta)[len(getTemposContrl(atleta)) - 1]
    
    s = str(posMeta).rjust(3)
    s += " | dorsal " + str(getDorsal(atleta)).rjust(3)
    s += " | " + converteHMS(tempoMeta)
    s += " | " + getNome(atleta)
    s += " (" + getEscalao(atleta) + ")"

    return s


def verificaTempoMin(atleta, controloInicial, controloFinal, tempoMinimo):
    """ Verifica se atleta percorreu um percurso num tempo >= tempoMinimo

    Verifica se o atleta percorreu um certo percurso num tempo igual ou 
    superior a tempoMinimo (medido em segundos).

    A medicao do tempo do percurso eh feita subtraindo o tempo de passagem
    no controlo controloInicial ao tempo de passagem no controlo controloFinal.
 
    Se o tempo do percurso especificado for igual ou superior a tempoMinimo,
    a funcao devolve True; caso contrario, a funcao devolve False. 
    Requires: atleta          seja um tuplo contendo informacao do atleta
              controloInicial seja um int com o numero do controlo inicial
              controloFinal   seja um int com o numero do controlo final
              tempoMinimo     seja um int com o tempo (em segundos) usado
                              para comparacao 
    Ensures:  True se atleta respeitou o tempo minimo, False no caso contrario
    """   
    # INSERIR CODIGO AQUI
    
    tempo = getTemposContrl(atleta)
    tempoFinal = tempo[controloFinal]
    tempoInicial = tempo[controloInicial]
    
    if ((tempoFinal - tempoInicial)>= tempoMinimo):
        return True
    else:
        return False

def setPosContrl(atleta, arrayPosContrl):
    """ Instancia lista com as posicoes do atleta em todos os controlos
 
    Usa uma matriz em que cada linha corresponde ao registo da ordem de
    passagem no controlo cujo numero eh dado pelo numero dessa linha.
    Requires: atleta sej um tuplo contendo informacao do atleta
              arrayPosContrl seja uma matriz que contem as posicoes de passagem
    Ensures:  instanciacao da lista com as posicoes do atleta em cada controlo
    """
    posContrl = []
    for i in range(len(arrayPosContrl)):
        posContrl.append(encontraPosicao(atleta, arrayPosContrl, i))

    atleta[3].extend(posContrl)


def setTemposContrl(atleta, arrayTemposContrl):
    """ Instancia lista com os tempos do atleta em todos os controlos
 
    Usa uma matriz em que cada linha corresponde ao registo dos tempos de
    passagem no controlo cujo numero eh dado pelo numero dessa linha.

    Os tempos sao registados pela mesma ordem em que os atletas passam no 
    controlo.
    Requires: atleta seja um tuplo contendo informacao do atleta
              arrayTemposContrl seja uma matriz que contem os tempos de passagem
    Ensures:  instanciacao da lista com os tempos do atleta em cada controlo
    """    
    temposContrl = []
    for i in range(len(arrayTemposContrl)):
        temposContrl.append(arrayTemposContrl[i][getPosContrl(atleta)[i]])

    atleta[4].extend(temposContrl)
                   

def converteHMS(segundos):
    """ Obtem a representacao textual do tempo medido em segundos

    A representacao fica no formato hh:mm:ss.    
    Requires: segundos seja um int contendo o tempo, em segundos, a converter
    Ensures:  string com a representacao textual do tempo
    """
    # INSERIR CODIGO AQUI
    
    return time.strftime('%H:%M:%S', time.gmtime(segundos))
