# coding: utf8

u"""Testes unitários às funções desenvolvidas pelos alunos em clima.py.

Importa as funções do módulo, com o objectivo principal de testar as funções
desenvolvidas pelos alunos:
-- clima (ficheiro clima.py)

Lê o ficheiro de texto:
-- temperaturas_desde_1800.csv

Cria o ficheiro de imagem:
-- temps_medias_anuais_desde_1800.png
"""

# no módulo clima optamos por nomes de funções não qualificados,
# por simplicidade, e porque não há risco de confusão
from clima import *

anos = range(1800, 2017)

# leitura dos dados do ficheiro temperaturas_desde_1800.csv
dados = ler_ficheiro("temperaturas_desde_1800.csv")

print "-- testando data_fraccionaria() ---"
print data_fraccionaria(1945, 3)
print data_fraccionaria(1952, 7)
print data_fraccionaria(2016, 8)

print "-- testando medias_anuais_alguns_paises() ---"
temps_med_anuais_Benelux = medias_anuais_alguns_paises(dados, anos,
                            ["Belgium and Luxemborg", "Netherlands"])
temps_med_anuais_Belgica_Luxemburgo = medias_anuais_alguns_paises(dados, anos,
                            ["Belgium and Luxemborg"])
print temps_med_anuais_Benelux[100]
print temps_med_anuais_Belgica_Luxemburgo[100]

print "-- testando medias_anuais() ---"
temps_med_anuais_todos = medias_anuais(dados, anos)
temps_med_anuais_Benelux = \
    medias_anuais(dados, anos, ["Belgium and Luxemborg", "Netherlands"])
temps_med_anuais_Belgica_Luxemburgo = \
    medias_anuais(dados, anos, ["Belgium and Luxemborg"])
print temps_med_anuais_todos[100]
print temps_med_anuais_Benelux[100]
print temps_med_anuais_Belgica_Luxemburgo[100]

print "-- testando medias_mensais_alguns_paises() ---"
temps_med_mensais_Benelux = medias_mensais_alguns_paises(dados, anos,
                            ["Belgium and Luxemborg", "Netherlands"])
temps_med_mensais_Belgica_Luxemburgo = medias_mensais_alguns_paises(dados, anos,
                            ["Belgium and Luxemborg"])
print temps_med_mensais_Benelux[1000]
print temps_med_mensais_Belgica_Luxemburgo[1000]

print "-- testando medias_mensais() ---"
temps_med_mensais_todos = medias_mensais(dados, anos)
temps_med_mensais_Benelux = medias_mensais(dados, anos,
                            ["Belgium and Luxemborg", "Netherlands"])
temps_med_mensais_Belgica_Luxemburgo = medias_mensais(dados, anos,
                            ["Belgium and Luxemborg"])
print temps_med_mensais_todos[1000]
print temps_med_mensais_Benelux[1000]
print temps_med_mensais_Belgica_Luxemburgo[1000]

print "-- testando medias_mensais_mes_especifico_alguns_paises() ---"
temps_med_mensais_Julho_Benelux = \
   medias_mensais_mes_especifico_alguns_paises(dados, anos,
                    ["Belgium and Luxemborg", "Netherlands"], 7)
temps_med_mensais_Julho_Belgica_Luxemburgo = \
   medias_mensais_mes_especifico_alguns_paises(dados, anos,
                    ["Belgium and Luxemborg"], 7)
print temps_med_mensais_Julho_Benelux[100]
print temps_med_mensais_Julho_Belgica_Luxemburgo[100]

print "-- testando escrever_ficheiro_data_fraccionaria() ---"
escrever_ficheiro_data_fraccionaria(dados,
                            "temperaturas_desde_1800-data_fraccionaria.csv")
espreitaAgora = open("temperaturas_desde_1800-data_fraccionaria.csv")
for i in range (10):
    espreitaAgora.readline()
linha = espreitaAgora.readline()
espreitaAgora.close()
print linha[:-1]  # eliminando o '\n' no fim
espreitaAgora = open("temperaturas_desde_1800-data_fraccionaria.csv")
print len(espreitaAgora.readlines())  # número de linhas do ficheiro
espreitaAgora.close()

print "-- testando temperatura() ---"
print temperatura(dados, 1945, 6, "France")

print "-- testando media_das_temperaturas_mensais() ---"
# fazendo um teste independente, é possível ter a certeza de que há medições
# de temperatura para este país no mês de Junho em todos os anos;
# esse teste não é feito aqui
print media_das_temperaturas_mensais(dados, anos, 6, "France")

print "-- testando max_das_temperaturas_mensais() ---"
print max_das_temperaturas_mensais(dados, anos, 6, "France")

print "-- testando mostra_grafico() ---"
temps_med_anuais_todos = medias_anuais_todos_paises(dados, anos)
temps_med_anuais_todos_5_abaixo = [x - 5 for x in temps_med_anuais_todos]
temps_med_mensais_todos = medias_mensais_todos_paises(dados, anos)
temps_med_mensais_todos_5_abaixo = \
                     [(x, y - 5) for (x, y) in temps_med_mensais_todos]
# criando ficheiro
mostra_grafico(u"Temperaturas médias anuais ao longo dos anos",
               "ao longo dos anos", u"temperaturas (graus centígrados)",
               [anos] * 2, [temps_med_anuais_todos,
                            temps_med_anuais_todos_5_abaixo],
               ["dados originais", "5 graus abaixo"],
               cria_ficheiro = True,
               nome_ficheiro = "duas_series_temporais")
print u"Verificar aparecimento de primeira janela com gráfico"
print "Verificar aparecimento de duas_series_temporais.png na pasta de trabalho"
# sem criar ficheiro
mostra_grafico(u"Temperaturas médias mensais  ao longo dos meses",
               "ao longo dos anos", u"temperaturas (graus centígrados)",
               [[p[0] for p in temps_med_mensais_todos],   \
                [p[0] for p in temps_med_mensais_todos_5_abaixo]],
               [[p[1] for p in temps_med_mensais_todos],   \
                [p[1] for p in temps_med_mensais_todos_5_abaixo]],
               ["dados originais", "5 graus abaixo"])
print u"Verificar aparecimento de segunda janela com gráfico"

