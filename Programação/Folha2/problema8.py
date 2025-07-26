##ano=int(input("Escreva um ano: "))
##if (ano>0):
##    if(ano%100==0):
##        print("O ano dado pertence ao século",ano//100)
##    else:
##        print("O ano dado pertence ao século",(ano//100 +1) )
##
##else:
##    print("O ano dado é igual ou menor que 0.")

ano=int(input("Escreva um ano: "))

a = int(ano%100 != 0)

print("O ano dado pertence ao século",ano//100 + a)
