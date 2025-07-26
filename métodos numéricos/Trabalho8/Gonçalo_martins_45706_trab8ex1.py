import math
import pylab
obama=[]
mccain=[]
with open("allwithoutnames.txt", "r") as ficheiro:
        l=ficheiro.readlines()
for i in l:
    obama.append(float(i.split()[0]))
    mccain.append(float(i.split()[1]))
#print obama
#print mccain
fv=[]
fv2=[]
for i in range(0,len(obama),1):
    fv.append(obama[i]/(obama[i]+mccain[i])-mccain[i]/(obama[i]+mccain[i]))
    if obama[i]+mccain[i]>20000:
        fv2.append(obama[i]/(obama[i]+mccain[i])-mccain[i]/(obama[i]+mccain[i]))
fvp=[]
fvn=[]
for i in range(0,len(fv),1):
    if fv[i]<0:
        fvn.append(fv[i])
    elif fv[i]>0:
        fvp.append(fv[i])

fvp2=[]
fvn2=[]
for i in range(0,len(fv2),1):
    if fv2[i]<0:
        fvn2.append(fv2[i])
    elif fv2[i]>0:
        fvp2.append(fv2[i])

pylab.hist(fvn2,bins=[-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0],histtype='bar',ec='black',color='b')
pylab.hist(fvp2,bins=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],histtype='bar',ec='black',color='g')
pylab.xlabel("diferenca fraccional entre obama e mccain",fontsize=18)
pylab.ylabel("numero de estados em que ocorre",fontsize=18)
pylab.show()
pylab.hist(fvn,bins=[-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0],histtype='bar',ec='black',color='b')
pylab.hist(fvp,bins=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],histtype='bar',ec='black',color='g')
pylab.xlabel("diferenca fraccional entre obama e mccain",fontsize=18)
pylab.ylabel("numero de estados em que ocorre",fontsize=18)
pylab.show()
        
