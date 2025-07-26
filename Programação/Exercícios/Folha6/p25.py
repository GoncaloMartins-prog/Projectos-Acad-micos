import copy
def swapSubListsCopy(l):
    """Trocam de posicoes a lista com maior soma e menor


    Requires: l ser uma lista de listas de inteiros
    Ensures: devolve a lista l mas duas das suas listas
             trocam de posicoes, nomeadamente, aquela
             cuja soma dos seus inteiros tem maior valor
             por aquela outra cuja soma dos seus inteiros
             tem menor valor
    """
    l_d = copy.deepcopy(l)
    maxi = sum([a for a in l_d[0]])
    l_maxi = l_d[0]
    mini = sum([b for b in l_d[0]])
    l_mini = l_d[0]
    indice_maxi = 0
    indice_mini = 0
    for i in l_d:
        soma = sum([e for e in i])
        indice = l_d.index(i)
        if soma > maxi:
            maxi = soma
            indice_maxi = indice
            l_maxi = i
        elif soma < mini:
            mini = soma
            indice_mini = indice
            l_mini = i
            
    l_d.insert(indice_maxi, l_mini) 
    l_d.pop((indice_maxi + 1)) 
    l_d.insert(indice_mini, l_maxi)
    l_d.pop(indice_mini + 1)
    
    return l_d

l_de_l = []
n_listas = int(input("Quantas listas tem a sua lista? "))
for i in range(n_listas):
    lista = []
    n_elementos = (int(input("Quantos elementos tem esta lista? ")))
    for e in range(n_elementos):
        lista.append(int(input("Insira um elemento da lista: ")))
    l_de_l.append(lista)
    
print(swapSubListsCopy(l_de_l))   
