k = int(input("Nº inteiro positivo: "))
x = k
nv = 0   #numero de vezes
while k%2 == 0 :
    k = k//2
    nv += 1
print("Consegues-se dividir", x,"exatamente", nv, "vez(es) por 2.")
