def mostra(nome_ficheiro):
    """Apresenta no ecra o programa em python sem os comentarios

    Requires: nome_ficheiro seja uma string que represente o nome
              de um ficheiro de texto na diretoria deste programa
              que tenha escrito um programa em python
    Side-effect: imprimir no ecra o programa escrito no ficheiro cujo
             nome eh dado, sem os comentarios, sendo que estes ocorrem
             em qualquer lugar de uma linha e sao assinalados pelo
             caracter #
    """
    f_dentro = open(nome_ficheiro, "r")
    codigo = ""
    for linha in f_dentro.readlines():
        comentario = False
        if codigo != "":
            if codigo[-1] != "\n":
                codigo += "\n"

        for caracter in linha:
            if caracter != "#" and not comentario:
                codigo += caracter

            else:
                comentario = True

    print(codigo)
    f_dentro.close()

mostra("programa_python.txt")
