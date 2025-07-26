import copy
def swapMaxMinCopy(l):
    """Troca de posicoes o maior e o menor elementos


    Requires: l ser uma lista de inteiros
    Ensures: devolve uma copia da lista igual a l mas
             onde o maior e o menor elemento
             trocam de posicoes
    """
    maxi = max(l)
    p_maxi = l.index(maxi)
    mini = min(l)
    p_mini = l.index(mini)
    l.insert(p_maxi, mini)
    l.pop(p_maxi+1)
    l.insert(p_mini, maxi)
    l.pop(p_mini+1)
    l_copia = copy.deepcopy(l)
    
    return l_copia

lista1 = []
n_elementos1 = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos1):
    lista1.append(int(input("Insira um elemento da lista: ")))
    
print(swapMaxMinCopy(lista1))   
