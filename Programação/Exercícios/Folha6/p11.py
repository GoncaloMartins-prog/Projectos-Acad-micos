def add_even(l):
    """

    Requires: l ser uma lista de inteiros
    Ensures: devolve a soma dos pares
             existente na lista
    """
    x = 0
    for i in l:
        if i%2 == 0:
            x += i
    return x 

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(add_even(lista))
