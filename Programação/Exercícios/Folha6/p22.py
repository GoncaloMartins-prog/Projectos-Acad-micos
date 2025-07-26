def swapMaxMin(l):
    """Troca de posicoes o maior e o menor elementos


    Requires: l ser uma lista de inteiros
    Ensures: devolve a lista l mas o maior e o menor
             elemento trocam de posicoes
    """
    #funciona
    p_menor = 0
    p_maior = 0
    maior = l[0]
    menor = l[0]
    for i in range(1, len(l)):
        if l[i] > maior:
            maior = l[i]
            p_maior = i
        elif l[i] < menor:
            menor = l[i]
            p_menor = i
    
    x = l[p_menor]
    l[p_menor] = l[p_maior]
    l[p_maior] = x
    return l
    
def swapMaxMin0(l):
    """Troca de posicoes o maior e o menor elementos


    Requires: l ser uma lista de inteiros
    Ensures: devolve a lista l mas o maior e o menor
             elemento trocam de posicoes
    """
    #funciona
    maxi = max(l)
    #print(maxi)
    p_maxi = l.index(maxi)
    #print(p_maxi)
    mini = min(l)
    #print(mini)
    p_mini = l.index(mini)
    #print(p_mini)
    l.insert(p_maxi, mini)
    l.pop(p_maxi + 1) 
    l.insert(p_mini, maxi)
    l.pop(p_mini + 1)
    
    return l

lista1 = []
n_elementos1 = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos1):
    lista1.append(int(input("Insira um elemento da lista: ")))
print(swapMaxMin(lista1))    
##swapMaxMin(lista1)
##print(lista1)
