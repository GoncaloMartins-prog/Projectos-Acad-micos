def append_list(l1, l2):
    """Devolve uma lista que eh a juncao de lista1 e lista2


    Requires: l1 e l2 serem duas listas
    Ensures: devolve uma lista resultante da juncao das duas
             listas originais
    """
    l_f = []
    for i in l1:
        l_f.append(i)
    for e in l2:
        l_f.append(e)
    return l_f

lista1 = [[1, 2, 3], 6, (8, 9)]
lista2 = [[5, 6], 8, 'sa', 'y']
##n_elementos1 = int(input("Quantos elementos tem a lista? "))
##for i in range(n_elementos1):
##    lista1.append(input("Insira um elemento da lista: "))
##
##n_elementos2 = int(input("Quantos elementos tem a outra lista? "))
##for i in range(n_elementos2):
##    lista2.append(input("Insira um elemento da outra lista: "))
print(append_list(lista1, lista2))
