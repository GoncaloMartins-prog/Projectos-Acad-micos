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

plt.plot(ano, wolf, color='blue')
plt.title("Evolução temporal do número de Wolf", fontsize = 18)
plt.xlabel("Ano", fontsize = 16)
plt.xlim(1740, 2000)
plt.ylabel("nº de Wolf", fontsize = 16)
plt.grid(linestyle=':')
plt.savefig('wolf.png')
plt.show()
    
