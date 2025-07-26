#5
i = 0
##n = int(input("Nº: "))
def retira(x):
    """Devolve o numero dado sem o digito da casa
    das unidades.

    Requires: x ser int positivo
    Ensures: o numero sem o algarismo das unidades
    """
    i = 0
    while (x>9):
        x = x-10
        i += 1
    return i

##print(":", retira(n))
##
##print()
def retira1(x):
    return x // 10
##print("O nº sem o alegarismo das unidades é: ", retira1(n))
##print()
def retira2(x):
    if x < 10:
        resultado = 0
    else :
        resultado = int(str(x)[:-1])
    return resultado
##print(":", retira2(n))
