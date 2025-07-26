def tsearch(tuplo, valor):
    """Determina o indice de t onde se encontra um determinado valor

    Requires: t seja um tuplo de inteiros e valor seja um int
    Ensures: devolve o indice (int) do tuplo t dado, onde esta um
             determinado valor, se nao encontrar devolve None
    """
    if valor in tuplo:
        indice = tuplo.index(valor)
    else:
        indice = None
    return indice

##tu = (1, 2, 3)
##va = 3
##print(tsearch(tu, va))
##print(tsearch(tu, 9))

e = int(input("Quantos elementos tem o tuplo? "))
t = ()
for i in range(e):
    ee = int(input("Indique um elemento (inteiro) do tuplo: "))
    t += (ee, )
print(t)
v = int(input("Valor do qual quer saber o indice no tuplo dado: "))
print(tsearch(t, v))

