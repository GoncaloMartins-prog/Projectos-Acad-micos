def tascii(tuplo):
    """

    Requires: 
    Ensures: construir um tuplo com os caracteres
             que têm o código ASCII entre 32 e
             127 inclusive 
    """
    tuplo_ascii = ()
    for i in tuplo:
        tuplo_ascii += (ord(i),)
    
    return tuplo_ascii

t = tuple(input("Escreva um tuplo: "))
print(t)
#[se escrever (1, 2) o t = ('(', '1', ',', ' ', '2', ')')]
print(tascii(t))
