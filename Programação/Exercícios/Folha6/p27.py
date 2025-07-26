import copy
def replaceCharsCopy(l):
    """Altera cada caracter pelo seu seguinte que dista três posicoes 

    Requires: recebe uma lista l, cujos elementos são caracteres
    Ensures: uma copia de l, mas em que cada caracter eh substituido
             pelo caracter seguinte no alfabeto que fica a três
             posições de distância
             (consideramos o alfabeto como sendo circular)
    """
    l_copia = copy.deepcopy(l)
    for i in range(len(l_copia)): #0, 1, 2, 3, 4, ...
        ordem_i = ord(l_copia[i])
        if 87 < ordem_i < 91 or 119 < ordem_i < 123:
            l_copia[i] = chr(ordem_i-23)
        else:
            l_copia[i] = chr(ordem_i+3)
    return l_copia

n_elementos = int(input("Quantos elementos tem a sua lista? "))
lista = []
for i in range(n_elementos):
    lista.append(input("Indique um caracter da sua lista: "))
print(lista)
print(replaceCharsCopy(lista))
print(lista)
