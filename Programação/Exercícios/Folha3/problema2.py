#n = 1.0
resposta = "Sim"
while (resposta == "Sim"):
    n = float(input("Introduza um número decimal(use . e não , pff): "))
    print("A parte inteira desse número é", int(n))
    resposta = input("Quer continuar a execução do programa? (Sim em caso afirmativo) ")
