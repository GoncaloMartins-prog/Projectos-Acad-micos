n1 = int(input("Escreva um número inteiro: "))
n2 = int(input("Escreva outro número inteiro: "))
n3 = int(input("Escreva ainda outro número inteiro: "))

if (n1 > n2 and n1 > n3):
    print("O número", n1, "é o maior dos três números que inseriu.")
elif (n2 > n1 and n2 > n3):
    print("O número", n2, "é o maior dos três números que inseriu.")
else:
    print("O número", n3, "é o maior dos três números que inseriu.")
