def swapSubLists(l):
    """Trocam de posicoes a lista com maior soma e menor


    Requires: l ser uma lista de listas de inteiros
    Ensures: devolve a lista l mas duas das suas listas
             trocam de posicoes, nomeadamente, aquela
             cuja soma dos seus inteiros tem maior valor
             por aquela outra cuja soma dos seus inteiros
             tem menor valor
    """
    maxi = sum([a for a in l[0]])
    l_maxi = l[0]
    mini = sum([b for b in l[0]])
    l_mini = l[0]
    indice_maxi = 0
    indice_mini = 0
    for i in l:
        soma = sum([e for e in i])
        print(soma)
        indice = l.index(i)
        if soma > maxi:
            maxi = soma
            indice_maxi = indice
            l_maxi = i
            print("aqui maximo", maxi, indice_maxi)
        elif soma < mini:
            mini = soma
            indice_mini = indice
            l_mini = i
            print("aqui minimo", mini, indice_mini)
        

    print("Maximo:", maxi)
    print("Posicao Maximo:", indice_maxi)
    print("Minimo:", mini)
    print("Posicao Minimo:", indice_mini)
    l.insert(indice_maxi, l_mini) #pk nao da (l.index(maxi), mini)??
    l.pop((indice_maxi + 1)) #pk nao da l.pop(l.index(mini)+1)
    l.insert(indice_mini, l_maxi)
    l.pop(indice_mini + 1)
    
    return l

l_de_l = []
n_listas = int(input("Quantas listas tem a sua lista? "))
for i in range(n_listas):
    lista = []
    n_elementos = (int(input("Quantos elementos tem esta lista? ")))
    for e in range(n_elementos):
        lista.append(int(input("Insira um elemento da lista: ")))
    print(lista)
    l_de_l.append(lista)
    
print(swapSubLists(l_de_l))   
