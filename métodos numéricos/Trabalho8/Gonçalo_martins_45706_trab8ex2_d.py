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

[ano, mes, wolf] = manchas_vs_tempo(lista)
f_t = wolf
f_t_T = []
for i in range(len(f_t)):
    f_t_T += [f_t[i] - f_t[i - 130]]
soma = 0
for i in f_t_T:
    soma += i
print(soma/len(f_t))

plt.plot(f_t_T, "b")
plt.grid(linestyle=':')
plt.title("nº de Wolf após aplicadas diferenças sazonais", fontsize = 18)
plt.xlabel("meses", fontsize = 16)
plt.ylabel("nº de Wolf", fontsize = 16)
plt.savefig('saz.png')
plt.show()
