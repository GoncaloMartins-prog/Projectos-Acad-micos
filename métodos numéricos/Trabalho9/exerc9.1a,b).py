import math
import matplotlib.pyplot as py
Massa=[400,70,45,2,0.3,0.16]
Metab=[270,82,50,4.8,1.45,0.97]
log_massa=[]
log_metab=[]
n=len(Massa)
for i in range(len(Massa)):
    log_massa.append(math.log(Massa[i]))
    log_metab.append(math.log(Metab[i]))

mlog_massa=sum(log_massa)/n
mlog_metab=sum(log_metab)/n
cov=0
var=0
for i in range(n):
    cov+=((log_metab[i]-mlog_metab)*(log_massa[i]-mlog_metab))/n
    var+=((log_massa[i]-mlog_massa)**2)/n

declive=cov/var
b=mlog_metab-declive*mlog_massa
list1=[]
list2=[]
a=math.exp(b)

for i in range(400):
    analitica=a*(i**(declive))
    list1.append(analitica)
    list2.append(i)
print(declive,b)
py.plot(Massa,Metab,'o',label='Dados recolhidos')
py.plot(list2,list1,label='Regressão linear')
py.xlabel('Massa (Kg)',fontsize=17)
py.ylabel('Metabolismo (W)',fontsize=17) 
py.rc('legend', fontsize=17)
py.tick_params(axis='both', which='major', labelsize=17)
py.legend()
py.show()



