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
n = int(input("Numero inteiro positivo: "))
print(eh_primo(n))
