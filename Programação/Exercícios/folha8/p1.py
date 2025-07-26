#dicionario para organizar os dados do meu cartao do cidadao
import datetime
def ler_cc():
    """Pede dados ao utilizador dados do cc e devolve um dicionario com eles

    Ensures: devolve um dicionario com os dados dados.
    """
    d = {}
    d['nome'] = input("Escreva o seu nome (sem apelido): ")
    d['apelido'] = input("O seu apelido: ")
##    d['numero'] = input("O seu numero de cc: ")
##    d['digitos_adicionais'] = input("Os digitos adicionais: ")
    d['nascimento'] = input('A sua data de nascimento(AAAA-MM-DD): ')
##    d['pai'] = input('O nome do seu pai: ')
##    d['mae'] = input('O nome da sua mae: ')
##    d['validade'] = input('A data de validade(AAAA-MM-DD): ')
    return d

def folga(cc):
    """Devolve o numero de dias que faltam para a validade do cc terminar

    Requires: cc seja um dicionario com os dados do cartao de cidadao, e que
              tenha nomeadamente a chave 'validade' associada ah data de
              validade do cc, e que o seu valor esteja na forma AAAA-MM-DD
              onde AAAA eh o ano, MM eh o mes e DD eh o dia
    Ensures: um inteiro que representa o numero de dias que faltam para
             o cc perder a validade
    """
    now = datetime.datetime.now()
    validade = cc['validade']
    n_dias = (now.year - int(validade[:4])) * 365 + \
             (now.month - int(validade[5:7])) * 30 + \
             (now.day - int(validade[8:]))
    return n_dias

def mais_novo(lista_ccs):
    """Diz quem é a pessoa mais nova

    Requires: lista_ccs seja uma lista de dicionarios com os dados de varios
              cartoes de cidadao, cada um desses dicionarios tem de ter a
              chave 'nascimento' associada ao valor que eh a data de
              nascimento da pessoa em causa, na forma AAAA-MM-DD, onde AAAA
              é o ano, MM eh o mes e DD o dia. Tambem tem de ter a chave 'nome'
              associada ao nome da pessoa em causa, e a chave 'apelido' ao
              apelido.
    Ensures: Percorre uma lista de ccs e devolve uma string com o nome e
             apelido da pessoa mais nova
    """
    now = datetime.datetime.now()
    nome_a = lista_ccs[0]['nome'] +' '+ lista_ccs[0]['apelido']

    data_nascimento_0 = lista_ccs[0]['nascimento']
    dias_vivo_menor = (now.year - int(data_nascimento_0[:4])) * 365 + \
                      (now.month - int(data_nascimento_0[5:7])) * 30 +\
                      (now.day - int(data_nascimento_0[8:]))
    
    for cc in lista_ccs[1:]:
        data_nascimento = cc['nascimento']
        dias_vivo = (now.year - int(data_nascimento[:4])) * 365 + \
                    (now.month - int(data_nascimento[5:7])) * 30 +\
                    (now.day - int(data_nascimento[8:]))
        if dias_vivo < dias_vivo_menor:
            dias_vivo_menor = dias_vivo
            nome_a = cc['nome'] +' '+ cc['apelido']
        

    return nome_a

##meu_cc = ler_cc()
##print(folga(meu_cc))
lista_de_ccs = []
qts_ccs = int(input("Quantos ccs quer analisar? "))
for i in range(qts_ccs):
    lista_de_ccs.append(ler_cc())
    print("===================")

print("A pessoa mais nova é ", mais_novo(lista_de_ccs))
