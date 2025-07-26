k = int(input("Escreva um número inteiro não-negativo: "))
r = "" #resposta
i = 2
while (k>i):
    if(k%i ==0):
        r = " não"
    i += 1
print(str(k)+ r +" é primo.")
