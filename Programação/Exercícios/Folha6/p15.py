def histogram(l):
    """Imprime o histograma de l


    Requires: l seja uma lista de inteiros
    Ensures: escreve no ecrã o histograma
             da lista dada, l
    """
    for x in l:
        print(x * "*")        
    
##    h = ""
##    for i in l[:-1:1]:
##        h = h + i*"*" + "\n"
##    h = h + l[-1]*"*"
##
##    print(h)

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
histogram(lista)
