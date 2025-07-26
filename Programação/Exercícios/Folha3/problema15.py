k = int(input("Escreva um número positivo, maior que 2: "))
i = 2
j = 2
quantos_num_p = 0
while(j <= k):
    s_divisores_proprios = 0
    i = 2
    while(i < j):
        if(j%i == 0 and i < j):
            s_divisores_proprios = s_divisores_proprios + i
        i += 1
    if(j == s_divisores_proprios + 1):
        quantos_num_p += 1
    j += 1
    
print("Entre 2 e", k, "existem", quantos_num_p, "números perfeitos.")
