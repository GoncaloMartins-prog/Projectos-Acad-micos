k = int(input("Nº inteiro positivo: "))
x = k
parte_inteira = 0
while k/2 >= 1 :
    k = k/2
    parte_inteira += 1
print("A parte inteira do logaritmo de", x,"de base 2 é", parte_inteira)
