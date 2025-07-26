def mostra(nome_ficheiro):
    """Apresenta no ecra o programa em python sem os comentarios nem docstrings

    Requires: nome_ficheiro seja uma string que represente o nome
              de um ficheiro de texto na diretoria deste programa
              que tenha escrito um programa em python
    Side-effect: imprimir no ecra o programa escrito no ficheiro cujo
             nome eh dado, sem os comentarios nem docstrings
    """
    f_dentro = open(nome_ficheiro, "r")
    codigo = ""
    docstring = False
    comentario = False
    for linha in f_dentro.readlines():
        
        indice = 0
        n_aspas = 0 #quando acaba a docsting para nao escrever essas 3 aspas
        #para haver sempre mudancas de linha 
        if comentario and codigo != "" and codigo[-1] != "\n":
            codigo += "\n"
            
        comentario = False        
        for caracter in linha:
            if n_aspas > 0:
                n_aspas += 1
                
            #ver se eh docstring
            if indice < len(linha)-2: #evita problemas de out of range na string
                if ((caracter == "\"" and linha[indice+1] == "\"" and \
                     linha[indice+2] == "\"") and not comentario):
                    
                    if not docstring:
                        docstring = True
                    else:
                        docstring = False
                        n_aspas = 1
                    
            #se nao for comentario adicionar ah string codigo
            if caracter != "#" and not comentario and not docstring and\
               (0 == n_aspas or n_aspas > 3):
                codigo += caracter

            #se nao for a nenhum das condicoes anteriores eh comentario
            elif caracter == "#":
                comentario = True
            
            indice += 1


    print(codigo)
    f_dentro.close()

mostra("programa_python.txt")

##(caracter ==  "\'" and \
##                     linha[indice+1] == "\'" and linha[indice+2] == "\'")
