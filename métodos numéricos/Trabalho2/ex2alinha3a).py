import math
#import pylab as plt
def f(x):
    return (math.tan(x)*90-
            (9.8/(2*30**2*math.cos(x)**2))*90**2 + 1-1.8)

lista_x2 = []
lista_y2 = []
xo = 5*math.pi/4
x1 = 4.2
fo = f(xo)
f1 = f(x1)
k = 0
d1 = f1 * ((x1 - xo) / (f1 - fo))

while abs(d1) > 10 ** -5 and k < 50:
    x2 = x1 - d1
    xo = x1
    x1 = x2
    fo = f1
    f1 = f(x1)
    fo = f(xo)
    d1 = f1 * ((x1 - xo) / (f1 - fo))
    k = k + 1
    print(" iterações secante= ", k, " critério= ", xo)
    lista_x2.append(k)
    lista_y2.append(d1)
    
#plt.plot(lista_x2, lista_y2, "b")
