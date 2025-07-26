def common_count(l1, l2):
    """Devolve um int com o numero de elementos iguais
        em ambas as listas


    Requires: l1 e l2 serem duas listas sem elementos
              repetidos
    Ensures: devolve quantos elementos as listas dadas,
             l1 e l2, vao ter em comum
    """
    n = 0
    for i in l1:
        for e in l2:
            if i == e:
                n += 1
    return n

lista1 = []
lista2 = []
n_elementos1 = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos1):
    lista1.append(int(input("Insira um elemento da lista: ")))

n_elementos2 = int(input("Quantos elementos tem a outra lista? "))
for i in range(n_elementos2):
    lista2.append(int(input("Insira um elemento da outra lista: ")))
print(common_count(lista1, lista2))
