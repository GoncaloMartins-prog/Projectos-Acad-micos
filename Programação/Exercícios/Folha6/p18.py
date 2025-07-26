import copy
def removeAllcopy(l, n):
    """Devolve uma lista sem todas as ocorrencias de n


    Requires: l seja uma lista de inteiros ordenada              
    Ensures: devolve uma lista onde todas as
             ocorrencias de n foram removidas
    """
    li = copy.deepcopy(l)
    for i in l:
        if i == n:
            li.remove(i)
    return li

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
num = int(input("Qual o número que deseja retirar? "))
print(removeAllcopy(lista, num))
