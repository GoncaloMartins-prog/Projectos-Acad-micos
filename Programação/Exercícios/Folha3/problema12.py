k= int(input("Escreva um número inteiro positivo: "))
s=0
i=2
while(i<k):
    if(k%i==0):
        s = s+i
    i +=1
    
print("A soma dos seus divisores próprios é", s)
