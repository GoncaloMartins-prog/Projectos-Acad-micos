n1=int(input("Escreva um número inteiro: "))
print ("O menor número lido até agora é", n1)

n2=int(input("Escreva um segundo número inteiro: "))
if(n1<n2):
       print ("O menor número lido até agora é", n1)
else:
    print ("O menor número lido até agora é", n2)
    
n3=int(input("Escreva ainda outro número inteiro: "))
if (n1<=n2 and n1<=n3):
    print("O menor número lido até agora é", n1)
elif (n2<=n1 and n2<=n3):
    print("O menor número lido até agora é", n2)
else :
    print("O menor número lido até agora é", n3)
    
n4=int(input("Escreva, por fim, outro número inteiro: "))
if (n1<=n2 and n1<=n3 and n1<=n4):
    print("O menor número lido até agora é", n1)
elif (n2<=n1 and n2<=n3 and n2<=n4):
    print("O menor número lido até agora é", n2)
elif (n3<=n1 and n3<=n2 and n3<=n4):
    print("O menor número lido até agora é", n3)
else:
    print("O menor número lido é", n4)
