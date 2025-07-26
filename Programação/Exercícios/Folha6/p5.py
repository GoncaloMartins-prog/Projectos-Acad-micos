def trepeat(n_componentes, valor):
    """

    Requires: n_componentes seja int
    Ensures: devolve um tuplo com a dimensão
             especificada (n_componentes) em
             que todas as componentes têm o
             valor passado como parâmetro
    """
    tuplo = ()
    for i in range(n_componentes):
        tuplo += (valor,)
    return tuplo

n_c = int(input("Quantas componentes? "))
v = input("Qual é o valor? ")
print(trepeat(n_c, v))
