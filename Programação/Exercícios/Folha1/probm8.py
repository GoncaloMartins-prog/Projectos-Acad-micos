#b)
segundos = int(input("Escreva um intervalo de tempo em segundos: "))
horas = segundos//3600
#minutos = (segundos%3600)//60
minutos = (segundos-horas*3600)//60
#restante = segundos - (horas * 3600 + minutos * 60)
segundos = segundos - horas*3600 - minutos*60
print("Esse intervalo de tempo tem", horas,"horas,", minutos, "minutos e",\
      segundos, "segundos.")


##a)
horas = int(input("Quantas horas tem o intervalo de tempo? "))
minutos = int(input("Quantos minutos tem o intervalo de tempo? "))
segundos = int(input("Quantos segundos tem o intervalo de tempo? "))
total = horas * 3600 + minutos * 60+ segundos
print("O seu intervalo de tempo tem ", total, "segundos")
print("O seu intervalo de tempo tem ", horas * 3600 + \
      minutos * 60+ segundos, "segundos")
