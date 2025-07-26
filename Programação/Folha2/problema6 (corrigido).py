ano = int(input("Escreva o ano em que nasceu: "))
mes = int(input("Escreva o mês em que nasceu (1 a 12): "))
dia = int(input("Escreva o dia em que nasceu (1 a 31): "))
ah= 2021
mh = 3  #6
dh = 1  #15
    
if mh-mes > 0 or (mh-mes==0 and dh-dia >= 0):
#ja fez anos este ano
    if ah - ano == 1:
        tanos = 'Tem 1 ano,'
    else:
        tanos = 'Tem ' + str(ah-ano) + ' anos,'
    if dh-dia >= 0:
    #p.ex. 6/1/1968
        tmes = str(mh-mes) + ' mes(es), e'
        tdia = str(dh-dia) + ' dia(s).'
    else:
    #p.ex. 20/1/1968
        tmes = str(mh-mes-1) + ' mes(es), e'
        if mh==1 or mh==2 or mh==4 or mh==6 or mh==8 \
           or mh==9 or mh==11:
        #mes anterior ter 31 dias
            tdia = str(31-dia+dh) + ' dia(s).'
        elif mh==5 or mh==7 or mh==10 or mh==12:
        #mes anterior ter 30 dias
            tdia = str(30-dia+dh) + ' dia(s).'
        else:
        #março que vem depois de fevereiro, mh==3
            if (ah%100 != 0 and ah%4 == 0) or \
               (ah%100 == 0 and ah%400 == 0):
            #ver Nota 1 no final
                tdia = str(29-dia+dh) + ' dia(s).'
            else:
                tdia = str(28-dia+dh) + ' dia(s).'
    
    
else: #ainda não fez anos (dh-dia < 0 and mh-mes < 0)
    if ah - ano == 1:
        tanos = 'Tem 1 ano,'
    else:
        tanos = 'Tem ' + str(ah-ano-1) + ' anos,'

    if dh-dia >= 0:
    #p.ex. 13/12/1989
        tmes = str(mes-mh) + ' mes(es), e'
        tdia = str(dh-dia) + ' dia(s).'
    else:
    #p.ex. 24/11/2002
        tmes = str(12-mes+mh-1) + ' mes(es), e'
        if mh==1 or mh==2 or mh==4 or mh==6 or mh==8 \
           or mh==9 or mh==11:
        #mes anterior ter 31 dias
            tdia = str(31-dia+dh) + ' dia(s).'
        elif mh==5 or mh==7 or mh==10 or mh==12:
        #mes anterior ter 30 dias
            tdia = str(30-dia+dh) + ' dia(s).'
        else:
        #março que vem depois de fevereiro, mh==3
            if (ah%100 != 0 and ah%4 == 0) or \
               (ah%100 == 0 and ah%400 == 0):
            #ver Nota 1 no final
                tdia = str(29-dia+dh) + ' dia(s).'
            else:
                tdia = str(28-dia+dh) + ' dia(s).'
    
    
print(tanos, tmes, tdia)

#Nota 1 (info do p9 da f2):
#Note que um ano (não secular) é bissexto se for divisível por 4.
#Os anos seculares são bissextos se forem divisíveis por 400.
