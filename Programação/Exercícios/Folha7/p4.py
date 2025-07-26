def n_espacos_brancos(nome_ficheiro):
    """Conta o numero de espacos brancos de ficheiro

    Require: nome_ficheiro seja uma string, que represente um
             nome de um ficheiro de texto existente na diretoria
             do programa
    Ensures: um int que representa o numero de espacos em
             branco no ficheiro dado
    """
    f_dentro = open(nome_ficheiro, "r")
    n = 0
    for linha in f_dentro.readlines():
        n += linha.count(" ")
    f_dentro.close()
    return n

def n_palavras(nome_ficheiro):
    """Conta o numero de palavras de ficheiro

    Requires: nome_ficheiro seja uma string, que represente um
              nome de um ficheiro de texto existente na diretoria
              do programa
    Ensures: um int que represente o numero de palavras em
             ficheiro
    """
    f_dentro = open(nome_ficheiro, "r")
    n = n_espacos_brancos(nome_ficheiro)
    f_dentro.close()
    return n+1

def info_relevante(nome_ficheiro):
    """escreve noutro ficheiro a informacao relevante de ficheiro

    Requires: nome_ficheiro seja uma string, que represente um
              nome de um ficheiro de texto existente na diretoria
              do programa
    Ensures: um ficheiro de texto com o nome informacao_relevante
             onde esta o nome de ficheiro na primeira linha, na
             segunda o numero de linhas de ficheiro, na terceira
             o numero de palavras, e por fim o numero de caracteres.
    """
    f_output = open("informacao_relevante", "w")
    f_input = open(nome_ficheiro, "r")
    f_output.write(nome_ficheiro + "\n")
    n_linhas = 0
    n_caracteres = 0
    for linha in f_input.readlines():
        n_linhas += 1
        for caracter in linha:
            n_caracteres += 1
    f_input.close()
    f_output.write("Numero de linhas: " + str(n_linhas) + "\n")
    f_output.write("Numero de palavras: " + str(n_palavras(nome_ficheiro)) +\
                    "\n")
    f_output.write("Numero de caracteres: " + str(n_caracteres) + "\n")
    f_output.close()


print(n_palavras("escrito.txt"))
##info_relevante("escrito.txt")
