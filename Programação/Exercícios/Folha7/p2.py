in_file = open("Music.txt", "r")
n = 0
for linha in in_file:
    print(n, linha[:-1])
    n += 1

#esta bem??
in_file.close()
