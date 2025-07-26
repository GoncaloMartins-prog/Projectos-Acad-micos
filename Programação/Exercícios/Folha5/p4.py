#4
##x = int(input())
def unidades(x):
    """Devolve o digito da casa das unidades de
    um numero inteiro positivo.

    Requires: x ser int possitivo
    Ensures: o algarismo das unidades desse numero
    """
    while (x>9):
        x = x-10
    return x
##print("unidades:", unidades(x))
