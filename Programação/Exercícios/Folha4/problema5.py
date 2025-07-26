k = int(input("Escreva um numero inteiro: "))
j = 0
for i in range(0, k+1, 3):
    if(i%2 != 0):
        j += 1
print(j)
