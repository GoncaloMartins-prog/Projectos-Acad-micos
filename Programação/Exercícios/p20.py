def linear_merge(l1, l2):
    """Devolve uma lista que eh a fusao de lista1 e lista2


    Requires: l1 e l2 serem duas listas ordenadas de
              inteiros 
    Ensures: devolve uma lista ordenada resultante da
             fusao das duas listas originais
    """
    l_f = []
    for i in l1:
        l_f.append(i)
    for e in l2:
        l_f.append(e)
    l_f.sort()
    return l_f

lista1 = []
lista2 = []
n_elementos1 = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos1):
    lista1.append(int(input("Insira um elemento da lista: ")))
lista1.sort()

n_elementos2 = int(input("Quantos elementos tem a outra lista? "))
for i in range(n_elementos2):
    lista2.append(int(input("Insira um elemento da outra lista: ")))
lista2.sort()
print(linear_merge(lista1, lista2))
