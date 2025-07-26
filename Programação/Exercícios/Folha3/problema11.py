djoao = int(input("Indique em que degrau o João começou: "))
djoana = int(input("Indique em que degrau a Joana começou: "))
i=0
mesmo_degrau =""
while(djoana > djoao):
    djoao = djoao+2
    djoana = djoana-1
if(djoao==djoana):
    mesmo_degrau=""
else:
    mesmo_degrau=" não"
print ("Imediatamente antes de se encontrarem, o João e a Joana \
estão, respetivamente, no degrau", djoao-2, "e", djoana+1,
       ". No degrau seguinte eles"+ mesmo_degrau,
       "estarão no mesmo degrau.")    
