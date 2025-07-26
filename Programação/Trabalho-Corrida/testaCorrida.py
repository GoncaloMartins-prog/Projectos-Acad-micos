""" Modulo de teste

Testa as funcoes desenvolvidas nos modulos atleta e corrida do trabalho
de Programacao I.
 
A execucao deste modulo deve originar output igual ao que estah resgistado
no ficheiro output.txt, fornecido aos alunos.
"""

import atleta
import corrida


fichAtletas = "atletas.txt"
fichsPos = ["controlo0-posicoes.txt", "controlo1-posicoes.txt", \
            "controlo2-posicoes.txt", "controlo3-posicoes.txt"]
fichsTempos = ["controlo0-tempos.txt", "controlo1-tempos.txt", \
               "controlo2-tempos.txt", "controlo3-tempos.txt"]

c = corrida.criaCorrida (fichAtletas, fichsPos, fichsTempos)

listaAtletas = corrida.getAtletas(c)
posicoesControlos = corrida.getArrayPos(c)
temposControlos = corrida.getArrayTempos(c)


# Testes de correccao da lista de atletas obtida na linha acima

print ("\nTeste com o dorsal 481:")
print ("HEITOR GOMES aparece como", atleta.getNome(listaAtletas[ 481 ]))
print ("VT2M aparece como", atleta.getEscalao(listaAtletas[ 481 ]))
print ("\nTeste com o dorsal 600:")
print ("DAVID FAUSTINO aparece como", atleta.getNome(listaAtletas[ 600 ]))
print ("VT3M aparece como", atleta.getEscalao(listaAtletas[ 600 ]))


# Teste de correccao das matrizes posicoesControlos e temposControlos
print ("\nNo controlo 2, posicao 100, temos o dorsal", \
      posicoesControlos[ 2 ][ 100 ], \
      "com o tempo", temposControlos[ 2 ][ 100 ])


# Testando a funcao converteHMS()
print ("\nNo controlo 2, posicao 100, temos o dorsal", \
      posicoesControlos[ 2 ][ 100 ],\
      "com o tempo", atleta.converteHMS( temposControlos[ 2 ][ 100 ]))


# Verificando que, na posicao a seguir a ultima posicao valida num certo
# controlo, a linha da matriz posicoesControlos nao contem mais elementos 
print ("\nNo controlo 2, posicao 209, temos o dorsal", \
      posicoesControlos[ 2 ][ 209 ], \
      "com o tempo", temposControlos[ 2 ][ 209 ])
if len(posicoesControlos[ 2 ]) == 210:
    print ("\nNo controlo 2, nao existe posicao 210")


# Testando a funcao encontraPosicao()
if atleta.encontraPosicao(listaAtletas[424], posicoesControlos, 2 ) != 0 :
    print ("\nO dorsal 424 ocorre no controlo 2, na posicao", \
        atleta.encontraPosicao(listaAtletas[424], posicoesControlos, 2 ))
else:
    print ("\nO dorsal 424 nao ocorre no controlo 2.")
    
print ("Se o dorsal 424 ocorre na posicao 198, esta correcto.")


if atleta.encontraPosicao(listaAtletas[599], posicoesControlos, 2 ) != 0 :
    print ("\nO dorsal 599 ocorre no controlo 2, na posicao", \
        atleta.encontraPosicao(listaAtletas[599], posicoesControlos, 2 ))
else:
    print ("\nO dorsal 599 nao ocorre no controlo 2.")

print ("Se o dorsal 599 nao ocorre no controlo 2, esta correcto.")


# Testando a funcao getTodosControlosValidos()
if atleta.getTodosControlosValidos(listaAtletas[424]) :
    print ("\nO dorsal 424 cumpriu todos os controlos.")
else:
    print ("\nO dorsal 424 falhou pelo menos 1 controlo.")

print ("Se o dorsal 424 cumpriu todos os controlos, esta correcto.")


if atleta.getTodosControlosValidos(listaAtletas[382]) :
    print ("\nO dorsal 382 cumpriu todos os controlos.")
else:
    print ("\nO dorsal 382 falhou pelo menos 1 controlo.")

print ("Se o dorsal 382 falhou pelo menos 1 controlo, esta correcto.")
print ("Na verdade, o dorsal 382 correu mas nao chegou ao fim.")


# Testando a funcao mostraSequenciaPosicoes().
atleta.mostraSequenciaPosicoes(listaAtletas[322])

# Testando a funcao verificaTempoMin().
# O tempo indicado corresponde ao obtido na mesma distancia a velocidade
# do recorde mundial da maratona em estrada.
if atleta.verificaTempoMin(listaAtletas[424], 2, 3, 2535):
    print ("\nO dorsal 424 cumpriu o tempo minimo entre controlos 2 e 3.")


## Testando novamente o metodo verificaTempoMin(), agora com um ritmo lento.
## Aqui, eh suposto o atleta gastar tempo inferior a 10000 para percorrer
## o percurso.
    
if not atleta.verificaTempoMin(listaAtletas[424], 2, 3, 10000 ) :
    print ("\nO dorsal 424 foi rapido q.b. entre controlos 2 e 3.")


# Escreve a classificacao final no ficheiro classificacaoGeral.txt.
corrida.escreveClassGeralFich(c, "classificacaoGeral.txt")


# Testando o metodo dorsalNaPosicaoNoEscalao()
print ("\nDorsal da atleta na 4a posicao do escalao VT2F:", \
      corrida.dorsalNaPosicaoNoEscalao(c, "VT2F", 4))
print ("Se for 298, esta correcto.")

if corrida.dorsalNaPosicaoNoEscalao(c, "VT2F", 8) == 0 :
    print ("\nHouve menos de 8 atletas VT2F a terminar a corrida.")

# Testando a funcao desenhaSequenciaPosicoes().
# Esta funcao eh a ultima a ser invocada pois a abertura da janela bloqueia
# o programa ate que a janela seja fechada.
atleta.desenhaSequenciaPosicoes(listaAtletas[322])

