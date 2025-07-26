# coding: utf8

u"""Processa dados de temperatura a partir de diversos ficheiros.

Importa as funções do seguinte módulo, úteis para o processamento dos dados:
-- clima (ficheiro clima.py)

Importa explicitamente o módulo de gráficos, o que não seria necessário
caso todos os gráficos fossem criados com a função mostra_grafico():
-- pylab

Lê os ficheiros de texto:
-- temperaturas_desde_1800.csv
-- temperaturas_desde_1890.csv

Cria o ficheiro de imagem:
-- temps_medias_anuais_desde_1890.png
"""

# no módulo clima optamos por nomes de funções não qualificados,
# por simplicidade, e porque não há risco de confusão
from clima import *

import pylab


# Processamento de dados usando as funções de clima

# Portugal não tem dados que recuem até 1800
#   Espanha começa em Janeiro de 1787
#   Portugal começa em Dezembro de 1854
# inicialmente queremos analisar (também) Portugal;
# portanto trabalhamos com o ficheiro que tem dados a partir de 1890

anos = range(1890, 2017)

# leitura dos dados do ficheiro temperaturas_desde_1890.csv
dados = ler_ficheiro("temperaturas_desde_1890.csv")

# criação de 4 séries temporais com médias anuais da temperatura
temps_med_anuais_todos = medias_anuais(dados, anos)
temps_med_anuais_Iberia = medias_anuais(dados, anos, ["Spain", "Portugal"])
temps_med_anuais_Espanha = medias_anuais(dados, anos, ["Spain"])
temps_med_anuais_Portugal = medias_anuais(dados, anos, ["Portugal"])

# visualização das 4 séries temporais com médias anuais da temperatura;
# é também criado um ficheiro de imagem
mostra_grafico(u"Temperaturas médias anuais",
               "anos", "temperaturas (Celsius)",
               [anos] * 4, [temps_med_anuais_todos, temps_med_anuais_Iberia, \
                      temps_med_anuais_Espanha, temps_med_anuais_Portugal],
               ["todos", u"Ibéria", "Espanha", "Portugal"],
               cria_ficheiro = True,
               nome_ficheiro = "temps_medias_anuais_desde_1890")

# a mesma visualização, para o caso de não estar implementada
# a função mostra_grafico();
# aqui dispensa-se as legendas e a criação de ficheiro
pylab.plot(anos, temps_med_anuais_todos)
pylab.plot(anos, temps_med_anuais_Iberia)
pylab.plot(anos, temps_med_anuais_Espanha)
pylab.plot(anos, temps_med_anuais_Portugal)
pylab.show()

# criação de 4 séries temporais com médias mensais da temperatura
temps_med_mensais_todos = medias_mensais(dados, anos)
temps_med_mensais_Iberia = medias_mensais(dados, anos,
                                                        ["Spain", "Portugal"])
temps_med_mensais_Espanha = medias_mensais(dados, anos, ["Spain"])
temps_med_mensais_Portugal = medias_mensais(dados, anos, ["Portugal"])

# visualização das 4 séries temporais com médias mensais da temperatura
mostra_grafico(u"Temperaturas médias mensais",
               "anos", u"temperaturas (Celsius)",
               [[p[0] for p in temps_med_mensais_todos],   \
                [p[0] for p in temps_med_mensais_Iberia],  \
                [p[0] for p in temps_med_mensais_Espanha], \
                [p[0] for p in temps_med_mensais_Portugal]],
               [[p[1] for p in temps_med_mensais_todos],   \
                [p[1] for p in temps_med_mensais_Iberia],  \
                [p[1] for p in temps_med_mensais_Espanha], \
                [p[1] for p in temps_med_mensais_Portugal]],
               ["todos", u"Ibéria", "Espanha", "Portugal"])

# a mesma visualização, para o caso de não estar implementada
# a função mostra_grafico();
# aqui dispensa-se as legendas
pylab.plot([p[0] for p in temps_med_mensais_todos],
           [p[1] for p in temps_med_mensais_todos])
pylab.plot([p[0] for p in temps_med_mensais_Iberia],
           [p[1] for p in temps_med_mensais_Iberia])
pylab.plot([p[0] for p in temps_med_mensais_Espanha],
           [p[1] for p in temps_med_mensais_Espanha])
pylab.plot([p[0] for p in temps_med_mensais_Portugal],
           [p[1] for p in temps_med_mensais_Portugal])
pylab.show()

# criação de 3 séries temporais com o valor da temperatura no mês de Junho,
# ao longo dos anos, apenas para países específicos
temps_med_mensais_Junho_Iberia = \
   medias_mensais_mes_especifico_alguns_paises(dados, anos,
                                               ["Spain", "Portugal"], 6)
temps_med_mensais_Junho_Espanha = \
   medias_mensais_mes_especifico_alguns_paises(dados, anos, ["Spain"], 6)
temps_med_mensais_Junho_Portugal = \
   medias_mensais_mes_especifico_alguns_paises(dados, anos, ["Portugal"], 6)

# visualização das 3 séries temporais com o valor da temperatura no mês de Junho,
# ao longo dos anos, apenas para países específicos
mostra_grafico(u"Temperaturas médias mensais em Junho",
               "anos", "temperaturas (Celsius)",
               [anos] * 3,
               [temps_med_mensais_Junho_Iberia,  \
                temps_med_mensais_Junho_Espanha, \
                temps_med_mensais_Junho_Portugal],
               [u"Ibéria", "Espanha", "Portugal"])

# a mesma visualização, para o caso de não estar implementada
# a função mostra_grafico();
# aqui dispensa-se as legendas
pylab.plot(anos, temps_med_mensais_Junho_Iberia)
pylab.plot(anos, temps_med_mensais_Junho_Espanha)
pylab.plot(anos, temps_med_mensais_Junho_Portugal)
pylab.show()

# escrita dos dados num ficheiro de texto, convertendo a temperatura para
# formato fraccionário
escrever_ficheiro_data_fraccionaria(dados,
                            "temperaturas_desde_1890-data_fraccionaria.csv")

# obtenção, a partir dos dados, da temperatura na Nova Zelândia em Abril de 1920
print (temperatura(dados, 1920, 4, "New Zealand"))

# obtenção, a partir dos dados, do valor médio da temperatura em Junho
# ao longo dos anos, em Portugal
print (media_das_temperaturas_mensais(dados, anos, 6, "Portugal"))

# obtenção, a partir dos dados, do valor máximo da temperatura em Junho
# ao longo dos anos, em Portugal
print (max_das_temperaturas_mensais(dados, anos, 6, "Portugal"))


# novo ficheiro de dados, recuando ao ano de 1800
# excluímos Portugal da análise porque não tem dados que recuem até 1800,
# e portanto foi propositadamente excluído do ficheiro

# novo intervalo de anos
anos_1800 = range(1800, 2017)

# leitura dos dados do ficheiro temperaturas_desde_1800.csv
dados_1800 = ler_ficheiro("temperaturas_desde_1800.csv")

# criação de uma série temporal com médias anuais da temperatura considerando
# todos os países que surgem nos dados
temps_med_anuais_todos_1800 = medias_anuais(dados_1800, anos_1800)

# visualização da série temporal, que acabou de ser criada,
# com médias anuais da temperatura
mostra_grafico(u"Temperaturas médias anuais",
               "anos", u"temperaturas (Celsius)",
               [anos_1800],
               [temps_med_anuais_todos_1800],
               [u"dados de 17 países"])

# a mesma visualização, para o caso de não estar implementada
# a função mostra_grafico();
# aqui dispensa-se as legendas
pylab.plot(anos_1800, temps_med_anuais_todos_1800)
pylab.show()
