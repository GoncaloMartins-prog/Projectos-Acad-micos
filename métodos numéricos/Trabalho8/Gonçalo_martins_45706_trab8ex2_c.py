import matplotlib.pyplot as plt
import statistics as s
with open("spots.txt", "r") as file:

    lista = [linha.split() for linha in file]

    file.close()

for i in range(len(lista)):
    for v in range(3):
        lista[i][v] = float(lista[i][v])


    
def manchas_vs_tempo(lista):
    
    lista_ano = [0]*len(lista)
    lista_mes = [0]*len(lista)
    lista_n_wolf = [0]*len(lista)
    k = 1

    for i in range(len(lista)):
        
        lista_ano[i] = lista[i][0] + lista[i][1]/12

        lista_mes[i] = k

        lista_n_wolf[i] = lista[i][2]

        k+= 1
        
    return [lista_ano, lista_mes, lista_n_wolf]

# primeiro pico mês - 149
# último pico mês - 2777
# quantidade de periodos - 20
# T = 131.4 meses

#ou
#o primeiro k máximo é o periodo depois da correlação
#T = 128 meses

[ano, mes, wolf] = manchas_vs_tempo(lista)
    
import math
cos1 = []
cos2 = []
cos3 = []
for i in range(len(mes)):
    
    cos1 += [10*math.cos(2*3.14*i/131.4)]
    cos2 += [100-50*math.cos(2*3.14*i/128)]
    cos3 += [10*math.cos(2*3.14*i/127)]
    
plt.plot(wolf, label="Wolf")
#plt.plot(cos1, label="T = 131.4 meses")
#plt.plot(cos2, label="T = 128 meses")
##plt.plot(cos3, label="T = 127 meses")
plt.title("Wolf vs Mes", fontsize = 20)
plt.xlabel("Mes", fontsize = 20)
plt.ylabel("Wolf", fontsize = 20)
plt.show()

