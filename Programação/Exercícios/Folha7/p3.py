in_file = open("escrito.txt", "w")
a_escrever = input("Escrever no doc (linha vazia para terminar): ")
in_file.write(a_escrever + "\n")
while(a_escrever != ""):
    a_escrever = input("Escrever no doc (linha vazia para terminar): ")
    in_file.write(a_escrever + "\n")
in_file.close()
