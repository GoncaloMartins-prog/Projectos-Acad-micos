def trange(fim, inicio, passo):
    """Range, mas com tuplo

    Requires: fim, inicio e passo sejam int
    Ensures: 
    """
    tuplo = tuple()
    for e in range(inicio, fim, passo):
        tuplo += (e,)
    return tuplo

i = int(input("inicio do range(0 por omissao): "))
f = int(input("fim do range: "))
p = int(input("passo do range(1 por omissao): "))
print(i)
print(f)
print(p)
print(trange(f, i, p))
