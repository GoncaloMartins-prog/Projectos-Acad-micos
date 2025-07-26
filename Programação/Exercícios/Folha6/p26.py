def replaceChars(l):
    """Altera cada caracter pelo seu seguinte que dista três posicoes 

    Requires: recebe uma lista l, cujos elementos são caracteres
    Side_effect: substitui cada caracter pelo caracter seguinte
             no alfabeto que fica a três posições de distância
             (consideramos o alfabeto como sendo circular)
    """
    for i in range(len(l)): #0, 1, 2, 3, 4, ...
        ordem_i = ord(l[i])
        if 87 < ordem_i < 91 or 119 < ordem_i < 123:
            l[i] = chr(ordem_i-23)
        else:
            l[i] = chr(ordem_i+3)

n_elementos = int(input("Quantos elementos tem a sua lista? "))
lista = []
for i in range(n_elementos):
    lista.append(input("Indique um caracter da sua lista: "))
print(lista)
replaceChars(lista)
print(lista)
