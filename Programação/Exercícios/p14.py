def palindromos(l_s):
    """Identifica as strings da lista que sao
    palindromos e tem mais de tres elementos


    Requires: l_s seja uma lista de strings
    Ensures: devolve uma lista com as strings,
             da lista inicial, l, que tem mais
             de tres elementos e sao um palindromo
             (ser igual de tras para a frente
             e de frente para tras)
    """
    l_palindromos = []
    for i in l_s:
        if i == i[::-1] and len(i) > 3:
            l_palindromos.append(i)

    return l_palindromos

lista = []
n_elementos = int(input("Quantos elementos tem a lista? "))
for i in range(n_elementos):
    lista.append(input("Insira um elemento da lista: "))
print(palindromos(lista))
