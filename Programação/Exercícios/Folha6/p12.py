def same_first_last(l):
    """

    Requires: l ser uma lista
    Ensures: devolve True se a lista tem mais
             de um elemento e o primeiro e o
             último elemento são iguais,
             e False caso contrário
    """
    r = False
    if len(l) > 1 and l[0] == l[-1]:
        r = True
    return r

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(same_first_last(lista))
