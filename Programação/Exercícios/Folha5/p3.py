#3
x = float(input())
y = float(input())
z = float(input())
def maior(x, y, z):
    """Devolve o maior numero dos três dados.

    Requires: x, y e z sejam int ou float, ordenaveis
    Ensures: o maior desses valores
    """
    if(x>=y and x>=z):
        maior = x
    elif(y>=x and y>=z):
        maior = y
    elif(z>=x and z>=y):
        maior = z
    return maior
print("Maior: ", maior(x, y, z))
