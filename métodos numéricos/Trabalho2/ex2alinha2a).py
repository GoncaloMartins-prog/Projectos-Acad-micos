import math
#import pylab as plt

def f(x):
    return 9*math.exp(-x)*math.sin(2*math.pi*x) - 1.5*10**-3

x = 0.75
flinha = (18*math.pi*math.exp(-x)*math.cos(2*math.pi*x) - 9*math.exp(-x)*math.sin(2*math.pi*x))
lista_x = []
lista_y = []

#metodo newton


fk = f(x)
k = 0
d = (fk / flinha)

while abs(d) > 10 ** -6 and k < 50:
    x = x - d
    fk = f(x)
    flinha = (18*math.pi*math.exp(-x)*math.cos(2*math.pi*x)- 9*math.exp(-x)*math.sin(2*math.pi*x))
    d = (fk / flinha)
    k = k + 1
    print(" iterações newton= ", k, " critério= ", x) 
    lista_x.append(k)
    lista_y.append(d)

#plt.plot(lista_x, lista_y, "r")
#plt.show()
