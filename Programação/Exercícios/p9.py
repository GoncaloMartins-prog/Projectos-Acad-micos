import random
def choose_in_collection(l):
    """

    Requires: l ser uma lista
    Ensures: devolve um elemento aleatório da lista l
    """
    return l[random.randrange(len(l))]

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(input("Insira um elemento da lista: "))
print(choose_in_collection(lista))
