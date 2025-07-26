import numpy as np
import matplotlib.pyplot as py
import cv2
img = cv2.imread('rocks.jpg')     
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
py.imshow(gray_img ,cmap = py.get_cmap('gray'))
py.xticks(fontsize=14)
py.yticks(fontsize=14)
list1=[]
py.show()
for i in range(len(gray_img)):
    for k in range(284):
        list1.append(gray_img[i][k]/255)

Inte_total=sum(list1)
media=sum(list1)/(len(gray_img)*284)
py.hist(list1,bins=255,histtype='bar',color='blue',ec='black')
py.xlabel('Nível de cinza', fontsize=18)
py.ylabel('Número de pixeis', fontsize=18)
py.xticks(fontsize=14)
py.yticks(fontsize=14)
py.show()
ret,tresh_gray=cv2.threshold(gray_img,58,225,cv2.THRESH_BINARY_INV)
print (media)
soma1=0
soma2=0
for i in range(len(tresh_gray)):
    for k in range(len(tresh_gray[0])):
        if tresh_gray[i][k]!=0:
            soma2+=1
        soma1+=1

porosidade=(soma2/soma1)*100
print(porosidade,soma2,soma1)
py.imshow(tresh_gray,cmap = py.get_cmap('gray'))
py.xticks(fontsize=14)
py.yticks(fontsize=14)
py.show()
    
