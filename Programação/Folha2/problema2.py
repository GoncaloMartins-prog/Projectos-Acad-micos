n1= int(input("Escreva um número inteiro: "))
n2= int(input("Escreva outro número inteiro: "))
n3= int(input("Escreva ainda outro número, pls: "))
s_pares=0
s_impares=0
if n1%2==0:
    s_pares = s_pares + n1
else:
    s_impares = s_impares +n1

if n2%2==0:
    s_pares = s_pares + n2
else:
    s_impares = s_impares +n2
    
if n3%2==0:
    s_pares = s_pares + n3
else:
    s_impares = s_impares +n3

print ("A soma dos números pares que forneceu é: " + str(s_pares))
print ("A soma dos números ímpares que forneceu é: " + str(s_impares))
