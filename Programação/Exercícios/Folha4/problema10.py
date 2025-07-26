n = int(input("Escreva um numero inteiro positivo: "))
m = int(input("Escreva um numero inteiro positivo: "))
j = 0
for i in range(0, n+1):
    j += i
    if (j<m):
        print(i)
