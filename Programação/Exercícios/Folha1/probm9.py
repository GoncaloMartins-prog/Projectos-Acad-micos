n=int(input("Escreva um número entre 0 e 999, pls: "))
c= n//100
d=(n-c*100)//10
u= n-(c*100 + d*10)
print("Esse número tem",c ,"centenas, ",d ,"dezenas e",u ,"unidades.")
