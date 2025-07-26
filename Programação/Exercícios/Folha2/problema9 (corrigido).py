ano = int(input("Escreva um ano (> 1900): "))
mes = int(input("Escreva um mês(1-12): "))
#dias = 0
if ((ano%400==0 or (ano%4==0 and ano != 0)) and mes==2):
    dias = 29
elif(mes == 2):
    dias = 28
elif(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    dias = 31
elif(mes==4 or mes==6 or mes==9 or mes==11):
    dias = 30

print("O mês", mes, "do ano", ano, "tem", dias, "dias.")
