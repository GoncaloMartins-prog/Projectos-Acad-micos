n1 = int(input())
n2 = int(input())
if(n1 == n2 == 0):
    print("iguais e ambos zero!")
elif(n1 == n2):
    print("iguais")
else:
    print((max(n1, n2)**2) * (n1**2))

##ou    
##elif(n1>n2):
##    print((n1**2)*(n1**2))
##elif(n1<n2):
##    print((n2**2)*(n1**2))
