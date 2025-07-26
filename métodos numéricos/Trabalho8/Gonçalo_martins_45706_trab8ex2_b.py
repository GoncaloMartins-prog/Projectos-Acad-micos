import matplotlib.pyplot as plt

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

[ano, mes, wolf] = manchas_vs_tempo(lista)

def Rk(y, k):
    y_media = 0
    
    for i in y:
        
        y_media += i
        
    y_media = y_media/len(y)
        
    N = len(y)
    
    numerador = 0

    denominador = 0
    
    for i in range(N-k):
        numerador += (y[i] - y_media)*(y[i+k] - y_media)

    for i in range(N):
        denominador += (y[i] - y_media)**2

    return (1/(N-k))*numerador/((1/N)*denominador)

def autocorrelação(y):
    
    lista_Rk = []
    
    for k in range(len(y)):
        lista_Rk += [Rk(y, k)]

    return lista_Rk

plt.plot(autocorrelação(wolf))
plt.title('Autocorrelação da evolução temporal do nº de Wolf', fontsize=18)
plt.xlabel('meses', fontsize=16)
plt.ylabel('autocorrelação', fontsize=16)
plt.grid(linestyle=':')
plt.savefig('auto.png')
plt.show()
        

    
