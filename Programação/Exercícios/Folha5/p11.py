def eh_primo(num):
    """Verifica se num eh primo

    Requires: num ser int positivo
    Ensures: devolver True se num for primo,
            False caso contrário
    """
    primo = True
    for i in range(2, num):
        if num%i == 0:
            primo = False
    return primo

def qts_primos(n):
    """Calcula quantos numeros primos existem entre n e 2

    Requires: n ser int >2
    Ensures: escreve no ecra quantos numeros primos estao
            entre 2 e n, inclusive
    """
    n_primos = 0
    for i in range(2, n+1):
        if eh_primo(i):
            n_primos += 1
    print("Entre 2 e", n, "(inclusive), existem", n_primos,"primos.")
k = int(input("Numero inteiro >0: "))
qts_primos(k)
