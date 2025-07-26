#2
x = float(input())
y = float(input())
def maior(x, y):
    """Devolve o maior numero dos dois dados.

    Requires: x e y sejam int ou float
    Ensures: devolve o maior deles
    """
    if(x>y):
        maior = x
    else:
        maior = y
    return maior
print("Maior: ", maior(x, y))

def menor(x, y):
    return -maior(-x, -y)
##    if (maior(x, y) == x):
##         menor = y
##    else:
##         menor = x
##    return menor
print("menor: ", menor(x, y))
