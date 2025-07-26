n = int(input("Inteiro positivo: "))
for i in range(n):
    for j in range(n):
        if (j%2==0 and i%2==0):
            print ("#", end = " ")
        else:
            print ("+", end = " ")
    print ()
