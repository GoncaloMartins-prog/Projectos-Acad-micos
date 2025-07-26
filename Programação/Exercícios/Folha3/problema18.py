print("Pense num número inteiro entre 0 e 100.")
maior = 100
menor = 0
r1=""
while(r1 != "certo" and menor!=maior):
    #print(maior, menor)
    n = round((maior+menor)/2)
    print("O número é o", str(n) + ".")
    r1 = input()
    if(r1 == "menor" or r1 == "-"):
        maior = n
    elif(r1 == "maior" or r1 == "+"):
        menor = n
    elif(r1 == "certo"):
        print("Yupiiii!!")
    else:
        print("Resposta inválida.")
    
print("Acabou, obrigada, cumprimentos.")
