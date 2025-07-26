def remove_adjacent(l):
    """Devolve uma lista sem numeros iguais adjacentes


    Requires: l seja uma lista de inteiros
    Ensures: devolve uma lista ajustada onde
             todos os numeros adjacentes iguais
             foram reduzidos a um unico elemento
    """
    l_a = []
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            l_a.append(l[i])
    l_a.append(l[-1])
    return l_a

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(remove_adjacent(lista))
