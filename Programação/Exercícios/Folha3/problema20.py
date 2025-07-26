k = int(input("Nº inteiro >10: "))
n_capicuas = 0
i = 10
while i < k:
    i += 1
    if str(i)[::-1] == str(i):
        n_capicuas += 1

print("Entre 10 e", k, "existem", n_capicuas, "capícua(s).")
