def mostra(nome_ficheiro):
    """Apresenta no ecra o programa em python sem os comentarios

    Requires: nome_ficheiro seja uma string que represente o nome
              de um ficheiro de texto na diretoria deste programa
              que tenha escrito um programa em python
    Side-effect: imprimir no ecra o programa escrito no ficheiro cujo
             nome eh dado, sem os comentarios, sendo que estes ocorrem
             apenas no inicio de uma linha e sao assinalados por um
             caracter #
    """
    f_dentro = open(nome_ficheiro, "r")
    for linha in f_dentro.readlines():
        if linha[0] != "#" and linha[-1] == "\n":
            print(linha[:-1])
        elif linha[0] != "#":
            print(linha)
    f_dentro.close()

mostra("programa_python.txt")
