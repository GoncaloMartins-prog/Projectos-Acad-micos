def find(n, l):
    """Ve se n esta na lista l

    Requires: l ser uma lista
    Ensures: devolve True se existir n em l
    """
    e = False
    for i in l:
        print(i, n)
        if i == n:
            e = True
    return e
lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(input("Insira um elemento da lista: "))
n_elemento = input("Elemento: ")
print(n_elemento)
print(lista)
print(find(n_elemento, lista))

