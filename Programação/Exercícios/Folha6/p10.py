def count_even1(l):
    """

    Requires: l ser uma lista de inteiros
    Ensures: devolve quantos numeros pares
             existem na lista l
    """
    x = 0
    for i in l:
        if i%2 == 0:
            x += 1
    return x
def count_even2(l):
    """

    Requires: l ser uma lista de inteiros
    Ensures: devolve quantos numeros pares
             existem na lista l
    """
    return sum([1 for i in l if i%2 == 0 ]) 

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(count_even1(lista))
print(count_even2(lista))
