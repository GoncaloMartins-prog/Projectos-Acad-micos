import random
import matplotlib.pyplot as plt

coordenadas = open("finland.txt","r")

X=[]
Y=[]
dados=[]

for linha in coordenadas:
        x,y=linha.split()
        dados.append([int(x),int(y)])
        X.append(int(x))
        Y.append(int(y))

print(max(X))
print(max(Y))
print(min(X))
print(min(Y))

fig=plt.figure()

#Alínea B


for K in [2,3]:
    Dim=2
    N=len(dados)
    Niter=10
    centroides = [[random.randint(599000,698000), random.randint(212000,315000)] for i in range (K)]
    label=[-1 for n in range(N)]
    for n in range(11): #Niter + 1
        conta=[0 for k in range(K)]
        for i in range(N):
            d=[0]*K 
            for k in range(K):
                d[k] = ((X[i]-centroides[k][0])**2 + (Y[i]-centroides[k][1])**2)
            k_min=d.index(min(d))
            label[i]=k_min
            conta[k_min] +=1
        centroides=[[0,0] for j in range(K)] 
        for a in range(N):
            for f in range(Dim):
                centroides[label[a]][f] += dados[a][f]/conta[label[a]]
    print(centroides)
    pontos = [[[], []] for k in range(K)]
    for i in range(N):
        pontos[label[i]][0].append(dados[i][0])
        pontos[label[i]][1].append(dados[i][1])
    colors = ['red','lime','blue']

    ax1=fig.add_subplot(1,2,k)
    
    for k in range(K):
        ax1.plot(pontos[k][1], pontos[k][0], '.', color = colors[k])
        ax1.title.set_text('{} cluters'.format(K))
        fig.suptitle('Utilizadores com 2 e 3 clusters', fontsize = 18)
        
plt.show()   


#Alínea C

fig1=plt.figure()
for Iter in [2,3,4,5]:
    Dim=2
    K=4
    N=len(dados)
    centroides=[[random.randint(599000, 698000), random.randint(212000, 315000)] for k in range(K)]
    label=[-1 for n in range(N)]
    for n in range(Iter+1):
        conta=[0 for k in range(K)]
        for i in range(N):
            d=[0]*K 
            for k in range(K):
                d[k] = ((X[i]-centroides[k][0])**2 + (Y[i]-centroides[k][1])**2)
            k_min=d.index(min(d))
            label[i]=k_min
            conta[k_min] +=1
        centroides=[[0,0] for j in range(K)]
        for a in range(N):
            for f in range(Dim):
                centroides[label[a]][f] += dados[a][f]/conta[label[a]]
    #print(centroides)
    pontos = [[[], []] for k in range(K)]
    for i in range(N):
        pontos[label[i]][0].append(dados[i][0])
        pontos[label[i]][1].append(dados[i][1])
    colors = ['red','blue','lime','fuchsia']
    
    ax=fig1.add_subplot(2,2,Iter-1)
    
    for k in range(K):
        ax.plot(pontos[k][1], pontos[k][0], '.', color = colors[k])
        ax.title.set_text('{} iterações'.format(Iter))
        fig1.suptitle('Utilizadores agrupados em 4 grupos para 2,3,4 e 5 iterações.', fontsize = 18)
        
plt.show()   
        



#Alínea D

fig=plt.figure()
def kmeans(dados):
    lista_k =[]
    lista_soma =[]
    for K in range(2, 21):
        Dim = 2
        N = len(dados)
        Niter = 10
        centroides = [[random.randint(599000, 698000), random.randint(212000, 315000)] for k in range(K)]
        label = [-1 for n in range(N)]
        soma = 0
        for n in range(11): #Niter + 1
            conta = [0 for k in range(K)]
            for i in range(N):
                d=[0]*K
                for k in range(K):
                    d[k] = ((X[i]-centroides[k][0])**2 + (Y[i]-centroides[k][1])**2)
                k_min=d.index(min(d))
                label[i]=k_min
                conta[k_min] +=1
            centroides = [[0, 0] for k in range(K)]
            for i in range(N):
                for d in range(Dim):
                    centroides[label[i]][d] += dados[i][d] / conta[label[i]]

        for i in range(N):
            for d in range(Dim):
                soma += (dados[i][d] - centroides[label[i]][d]) ** 2
            
        lista_k.append(K)
        lista_soma.append(soma)
    return (lista_k, lista_soma)
res = kmeans(dados)
plt.plot(res[0], res[1], '-co')
plt.grid(True)
plt.title('Distância ao quadrado em função de k')
plt.xlabel('k')
plt.ylabel('Distância ao quadrado')
plt.show()





























