k = int(input("Escreva um número inteiro: "))
cubo = " não"
i = 0
while(i < k):
    if(k**(1/3) == i):
        cubo = ""
    i += 1

print(str(k)+cubo ,"é um cubo perfeito.")
