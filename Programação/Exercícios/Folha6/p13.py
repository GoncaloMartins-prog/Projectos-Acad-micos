def same_first_last(l):
    """

    Requires: l ser uma lista
    Ensures: devolve True se a lista tem mais
             de um elemento e o primeiro e o
             último elemento são iguais,
             e False caso contrário
    """
    r = False
    if len(l) > 1 and l[0] == l[-1]:
        r = True
    return r
def symmetrical(l):
    """Verifica se l eh igual ah sua inversa

    Requires: l seja uma lista
    Ensures: devolver True se a lista dada, l
             for igual ah sua inversa, e False
             caso contrario
    """
    res = True
    for i in range(len(l)//2):
        if same_first_last(l)== False:
            res = False
        l.pop(0)
        l.pop() #quando omitido assume-se -1
    return res

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(int(input("Insira um elemento da lista: ")))
print(symmetrical(lista))
