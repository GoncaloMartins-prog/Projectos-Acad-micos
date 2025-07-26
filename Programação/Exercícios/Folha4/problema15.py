seq = input("Insira uma sequência de caracteres: ")
dim  = len(seq)
for i in range(dim):
    print (seq[-1-i]) #-1, -2, ..., -8

print ("Alternativa")
for i in range(dim-1,-1, -1):
    print(seq[i])

print("outra")
for i in range(dim): 
    print(seq[dim-i-1])
