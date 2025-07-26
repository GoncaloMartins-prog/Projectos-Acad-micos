n = int(input("Escreva um numero inteiro: "))
j = 0
for i in range(1, n):
    if (n%i == 0):
        j += i
print(j)
