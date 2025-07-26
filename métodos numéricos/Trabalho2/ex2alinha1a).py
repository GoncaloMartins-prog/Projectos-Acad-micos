def f(x):
    return x**2 -4

import math
import pylab as plt

lista_x1=[]
lista_y1=[]

a1 = 0.7
b1 = 2.6
d1 = (b1-a1)/2
x1 = a1 + d1
n1 = 0

fa1 = f(a1)
fb1 = f(b1)

while d1 > 10**-5:
    fx1 = f(x1)
    if fa1 * fx1 > 0:
        a1 = x1
        fa1 = fx1
    else:
        b1 = x1
        fb1 = fx1
    d1 = (b1-a1)/2
    x1 = a1 + d1
    n1 = n1 + 1
    print( " interassao bissessao= ", n1, "criterio= ", d1)
    lista_x1.append(n1)
    lista_y1.append(d1)

plt.plot(lista_x1, lista_y1, "r")

lista_x2=[]
lista_y2=[]

a2 = 0.4
b2 = 1.7
d2 = (b2-a2)/2
x2 = a2 + d2
n2 = 0

fa2 = f(a2)
fb2 = f(b2)

while d2 > 10**-5:
    fx2 = f(x2)
    if fa2 * fx2 > 0:
        a2 = x2
        fa2 = fx2
    else:
        b2 = x2
        fb2 = fx2
    d2 = (b2-a2)/2
    x2 = a2 + d2
    n2 = n2 + 1
    print( " interassao bissessao= ", n2, "criterio= ", d2)
    lista_x2.append(n2)
    lista_y2.append(d2)

plt.plot(lista_x2, lista_y2, "b")

lista_x3=[]
lista_y3=[]

a3 = -3
b3 = 0.6
d3 = (b3-a3)/2
x3 = a3 + d3
n3 = 0

fa3 = f(a3)
fb3 = f(b3)

while d3 > 10**-5:
    fx3 = f(x3)
    if fa3 * fx3 > 0:
        a3 = x3
        fa3 = fx3
    else:
        b3 = x3
        fb3 = fx3
    d3 = (b3-a3)/2
    x3 = a3 + d3
    n3 = n3 + 1
    print( " interassao bissessao= ", n3, "criterio= ", d3)
    lista_x3.append(n3)
    lista_y3.append(d3)

plt.xlabel('iteracao bissecao')
plt.ylabel('criterio')
plt.plot(lista_x3, lista_y3, "g")
plt.show()


