def f(x):
    return x**2 - 4

import math
import pylab as plt

lista_x = []
lista_y = []

#metodo newton

x = 1.0
fk = f(x)
k = 0
d = (fk / (2.0 * x))

while abs(d) > 10 ** -5 and k < 50:
    x = x - d
    fk = f(x)
    d = (fk / (2.0 * x))
    k = k + 1
    print(" iterações newton= ", k, " critério= ", math.log(d)) 
    lista_x.append(k)
    lista_y.append((d))

plt.plot(lista_x, lista_y, marker='o', color='r')
#plt.show()

lista_x2 = []
lista_y2 = []

#metodo secante

xo = 3.0
x1 = 4.0
fo = f(xo)
f1 = f(x1)
l = 0
d1 = f1 * ((x1 - xo) / (f1 - fo))

while abs(d1) > 10 ** -5 and l < 50:
    x2 = x1 - d1
    xo = x1
    x1 = x2
    fo = f1
    f1 = f(x1)
    fo = f(xo)
    d1 = f1 * ((x1 - xo) / (f1 - fo))
    l = l + 1
    print(" iterações secante= ", l, " critério= ", math.log(d1))
    lista_x2.append(l)
    lista_y2.append((d1))
    
plt.plot(lista_x2, lista_y2, marker='o', color='b')

#metodo bisseção

lista_x3 = []
lista_y3 = []


a = -3
b = 0.6
d2 = (b - a) / 2
x3 = a + d2
n = 0

fa = f(a)
fb = f(b)

while d2 > 10 ** -5:
    fx = f(x3)
    if fa * fx > 0:
        a = x3
        fa = fx
    else:
        b = x3
        fb = fx
    d2 = (b - a) / 2
    x3 = a + d2
    n = n + 1
    print(" iterações bisseção= ", n, " critério= ", math.log(d2))
    lista_x3.append(n)
    lista_y3.append((d2))

plt.plot(lista_x3, lista_y3,marker='o', color='g')

plt.title('Erro do método em função do número de iterações', fontsize=14)
plt.xlabel('número de iterações',fontsize=14)
plt.ylabel('erro ( em escala log)',fontsize=14)
plt.yscale('log')
plt.xscale('linear')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

