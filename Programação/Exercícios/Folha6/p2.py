def tdiv(n):
    tuplo = tuple()
    for i in range (1, n+1):
        if n % i == 0:
            tuplo += (i,)
            #não estamos a mudar o tuplo mas sim a criar um novo
            #que resulta do que temos antes só com mais um elemento no fim
    return tuplo

x = int(input("Número inteiro >0:"))
print(tdiv(x))
