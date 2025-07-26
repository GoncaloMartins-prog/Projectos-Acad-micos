def succ(num):
    """Devolve o inteiro seguinte

    Requires: num seja um numero inteiro
    Ensures: devolver o inteiro seguinte
    """
    return num+1
n = int(input("Numero inteiro: "))
print("Inteiro seguinte: ", succ(n))
