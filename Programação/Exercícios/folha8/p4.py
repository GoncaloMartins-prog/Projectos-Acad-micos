def ficheiro_dic(nome_fich):
    """Devolve um dicionario com cada uma das palavras do texto associada ah
    lista de lonhas em que ocorre no texto

    Requires: nome_fich seja uma string com o nome de um ficheiro de texto
              acessivel por este programa
    Ensures: um dicionario com cada uma das palavras do texto em fich_texto
             associada ah lista de linhas em que ocorre no texto
    """
    #esta um bocado confuso e provavelmente
    #complicado de mais desnecesaariamente
    fich_aqui = open(nome_fich, "r")
    dict_r = {}
    n_linha = -1  #a primeira linha eh a 0
    espacos = [' ', '\n', '\r', '\t']
    for linha in fich_aqui.readlines():
        n_linha += 1
        palavra = ""
        for caracter in linha:
            #se o caracter fizer parte de uma palavra
            if caracter not in espacos:  
                palavra += caracter
            elif palavra != "":
                #se for a primeira vez que a palavra aparece
                if dict_r.get(palavra, 0) == 0:
                    l_palavra = [] #defenimos
                else:
                    l_palavra = dict_r[palavra]
                l_palavra.append(n_linha)
                dict_r[palavra] = l_palavra
                palavra = ""
            
    if caracter not in espacos:
        if dict_r.get(palavra, 0) == 0:
            l_palavra = []
        l_palavra.append(n_linha)
        dict_r[palavra] = l_palavra
    fich_aqui.close()    
    return dict_r
    
print(ficheiro_dic("p4.txt"))
