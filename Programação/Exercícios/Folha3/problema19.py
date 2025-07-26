k = int(input("Escreva um número inteiro maior que 2: "))
i = 2
j = 2
primo = True
sp = 0   #soma dos primos
while (k>=i):
    j = 2
    primo = True
    while(i//2>=j):
        if(i%j == 0 and i != j):
            primo = False
        j += 1
    if(primo):
        sp += 1
    i += 1
print("Entre 2 e", k, "existem",sp ,"números primos.")
