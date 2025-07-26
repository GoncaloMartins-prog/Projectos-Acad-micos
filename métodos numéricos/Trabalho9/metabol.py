from math import log, exp, sqrt
import statistics as s
def deriv_dm(m0, b0, y, x):
    soma=0
    n=len(y)
    for i in range(n):
        soma+=(y[i]-m0*x[i]-b0)*x[i]
    return -2*soma/n
def deriv_db(m0, b0, y, x):
    soma=0
    n=len(y)
    for i in range(n):
        soma+=(y[i]-m0*x[i]-b0)
    return -2*soma/n

def grad(deriv_dm, deriv_db, m0, b0, lamb, eps, k_max):
    dm=deriv_dm(m0, b0, y, x)
    db=deriv_db(m0, b0, y, x)
    m1=m0-lamb*dm
    b1=b0-lamb*db
    k=0
    while (abs(lamb*sqrt(dm*dm+db*db))>eps and k<k_max):
        m0=m1
        b0=b1
        dm=deriv_dm(m0, b0, y, x)
        db=deriv_db(m0, b0, y, x)
        m1=m0-lamb*dm
        b1=b0-lamb*db
        k=k+1
    return m1, b1
y=[]
x=[]
met=open('metabol.txt')
for line in met:
    l=line.split()
    x.append(log(float(l[0])))
    y.append(log(float(l[1])))
print('$\lamba$ & $m$ & $b$')
for lam in [0.01, 0.05, 0.1]:
    (m, b)=grad(deriv_dm, deriv_db, 0, 0, lam, 1e-6, 100)
   
    print(str(lam)+' & '+str(m)+' & '+str(b)+'\\ \hline')

def mq(y, x):
    ym=s.mean(y)
    xm=s.mean(x)
    sum1=0
    sum2=0
    for i in range(len(x)):
        sum1+=(x[i]-xm)*(y[i]-ym)
        sum2+=(x[i]-xm)**2
    m=sum1/sum2
    b=ym-m*xm
    return m, b
print(mq(y, x))








        
