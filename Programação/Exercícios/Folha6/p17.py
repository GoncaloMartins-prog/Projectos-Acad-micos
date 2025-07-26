def count_adjacent(l):
    """Devolve uma lista com tuplos representando
        quantas vezes um int ocorre na lista


    Requires: l seja uma lista de inteiros ordenada
    Ensures: devolve uma lista de tuplos onde o
             primeiro elemento eh o inteiro e
             o segundo o numero de vezes que ele
             ocorre na lista
    """
    l_t = []
    n = 1
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            n += 1
        elif l[i] != l[i+1]:
            l_t.append((l[i], n))
            n = 1
    return l_t

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
lista.sort()
lista.append(" ")
print(count_adjacent(lista))
